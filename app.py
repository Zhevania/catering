import os
from datetime import datetime, timedelta, timezone
from functools import wraps

from flask import (Flask, request, redirect, url_for, session, flash,
                   render_template, jsonify)
from jinja2 import DictLoader
from werkzeug.security import check_password_hash

from db import get_conn, init_db
from logic import (hitung_paket, hitung_dus, validasi_pilihan, status_pengingat,
                   MENU_PAKET, HARGA_PAKET, MIN_PAX, JUMLAH_MENU)
from templates import TEMPLATES

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "catering-umkm-dev-key")
app.jinja_loader = DictLoader(TEMPLATES)
app.jinja_env.globals.update(MENU_PAKET=MENU_PAKET, HARGA_PAKET=HARGA_PAKET,
                             MIN_PAX=MIN_PAX, JUMLAH_MENU=JUMLAH_MENU)

TZ = timezone(timedelta(hours=int(os.getenv("TZ_OFFSET", "8"))))  # WITA
BULAN = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]


@app.template_filter("rupiah")
def rupiah(n):
    return "Rp" + f"{int(n or 0):,}".replace(",", ".")


@app.template_filter("tgl")
def tgl(d):
    return f"{d.day} {BULAN[d.month - 1]} {d.year}" if d else "-"


@app.template_filter("daftar")
def daftar(s):
    return [x for x in (s or "").split("|") if x]


def hari_ini():
    return datetime.now(TZ).date()


def query(sql, params=(), commit=False, one=False):
    conn = get_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute(sql, params)
    if commit:
        conn.commit()
        result = cur.lastrowid
    else:
        result = cur.fetchone() if one else cur.fetchall()
    cur.close()
    conn.close()
    return result


def login_required(f):
    @wraps(f)
    def wrapper(*a, **kw):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*a, **kw)
    return wrapper


def daftar_pengingat():
    today = hari_ini()
    rows = query(
        "SELECT * FROM pesanan WHERE status='Baru' AND tanggal_acara IN (%s, %s) ORDER BY tanggal_acara, id",
        (today, today + timedelta(days=1)),
    )
    for r in rows:
        r["pengingat"] = status_pengingat(r["tanggal_acara"], today)
    return rows


def _nama(f):
    nama = f.get("pelanggan", "").strip()
    if not nama:
        raise ValueError("Nama pelanggan wajib diisi")
    return nama


# ---------- Auth ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = query("SELECT * FROM users WHERE username=%s",
                  (request.form.get("username", "").strip(),), one=True)
        if u and check_password_hash(u["password_hash"], request.form.get("password", "")):
            session["user"] = u["username"]
            return redirect(url_for("index"))
        flash("Username atau password salah", "error")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ---------- Dashboard ----------
@app.route("/")
@login_required
def index():
    q = request.args.get("q", "").strip()
    st = request.args.get("status", "")
    sql, params = "SELECT * FROM pesanan WHERE 1=1", []
    if q:
        sql += " AND (pelanggan LIKE %s OR menu LIKE %s)"
        params += [f"%{q}%", f"%{q}%"]
    if st:
        sql += " AND status=%s"
        params.append(st)
    sql += " ORDER BY (tanggal_acara IS NULL), tanggal_acara ASC, id DESC"
    rows = query(sql, params)
    today = hari_ini()
    for r in rows:
        r["pengingat"] = status_pengingat(r["tanggal_acara"], today) if r["status"] == "Baru" else None

    semua = query("SELECT total, status FROM pesanan")
    notif = daftar_pengingat()
    stats = {
        "total": len(semua),
        "proses": sum(1 for s in semua if s["status"] == "Baru"),
        "selesai": sum(1 for s in semua if s["status"] == "Selesai"),
        "pendapatan": sum(s["total"] for s in semua if s["status"] == "Selesai"),
    }
    return render_template("dashboard.html", rows=rows, stats=stats, notif=notif,
                           q=q, st=st, user=session["user"], today=tgl(today))


# ---------- Tambah pesanan ----------
@app.route("/tambah_paket", methods=["POST"])
@login_required
def tambah_paket():
    try:
        f = request.form
        nama = _nama(f)
        pax = int(f["pax"])
        pilihan = validasi_pilihan(f.getlist("menu"))
        total = hitung_paket(pax)
        query("INSERT INTO pesanan (pelanggan,menu,jumlah,harga_satuan,total,tanggal_acara,jenis,pilihan_menu) "
              "VALUES (%s,%s,%s,%s,%s,%s,'Paket',%s)",
              (nama, f"Paket Prasmanan {JUMLAH_MENU} Menu", pax, HARGA_PAKET, total,
               f.get("tanggal") or None, "|".join(pilihan)), commit=True)
        flash("Pesanan paket berhasil ditambahkan", "ok")
    except (ValueError, KeyError) as e:
        flash(f"Gagal: {e}", "error")
    return redirect(url_for("index"))


@app.route("/tambah_dus", methods=["POST"])
@login_required
def tambah_dus():
    try:
        f = request.form
        nama = _nama(f)
        menu = f.get("menu", "").strip()
        if not menu:
            raise ValueError("Nama menu dus wajib diisi")
        jumlah, harga = int(f["jumlah"]), int(f["harga"])
        total = hitung_dus(jumlah, harga)
        query("INSERT INTO pesanan (pelanggan,menu,jumlah,harga_satuan,total,tanggal_acara,jenis) "
              "VALUES (%s,%s,%s,%s,%s,%s,'Dus')",
              (nama, menu, jumlah, harga, total, f.get("tanggal") or None), commit=True)
        flash("Pesanan dus berhasil ditambahkan", "ok")
    except (ValueError, KeyError) as e:
        flash(f"Gagal: {e}", "error")
    return redirect(url_for("index"))


# ---------- Edit, selesai, hapus ----------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    p = query("SELECT * FROM pesanan WHERE id=%s", (id,), one=True)
    if not p:
        flash("Pesanan tidak ditemukan", "error")
        return redirect(url_for("index"))
    if request.method == "POST":
        try:
            f = request.form
            nama, tanggal = _nama(f), f.get("tanggal") or None
            if p["jenis"] == "Paket":
                pax = int(f["pax"])
                pilihan = validasi_pilihan(f.getlist("menu"))
                total = hitung_paket(pax)
                query("UPDATE pesanan SET pelanggan=%s, jumlah=%s, harga_satuan=%s, total=%s, "
                      "tanggal_acara=%s, pilihan_menu=%s WHERE id=%s",
                      (nama, pax, HARGA_PAKET, total, tanggal, "|".join(pilihan), id), commit=True)
            else:
                menu = f.get("menu", "").strip()
                if not menu:
                    raise ValueError("Nama menu dus wajib diisi")
                jumlah, harga = int(f["jumlah"]), int(f["harga"])
                total = hitung_dus(jumlah, harga)
                query("UPDATE pesanan SET pelanggan=%s, menu=%s, jumlah=%s, harga_satuan=%s, total=%s, "
                      "tanggal_acara=%s WHERE id=%s",
                      (nama, menu, jumlah, harga, total, tanggal, id), commit=True)
            flash("Pesanan berhasil diperbarui", "ok")
            return redirect(url_for("index"))
        except (ValueError, KeyError) as e:
            flash(f"Gagal: {e}", "error")
    return render_template("edit.html", p=p, user=session["user"])


@app.route("/status/<int:id>", methods=["POST"])
@login_required
def status(id):
    query("UPDATE pesanan SET status='Selesai' WHERE id=%s", (id,), commit=True)
    flash("Pesanan ditandai selesai", "ok")
    return redirect(request.referrer or url_for("index"))


@app.route("/hapus/<int:id>", methods=["POST"])
@login_required
def hapus(id):
    query("DELETE FROM pesanan WHERE id=%s", (id,), commit=True)
    flash("Pesanan dihapus", "ok")
    return redirect(url_for("index"))


# ---------- Pemberitahuan ----------
@app.route("/api/notifikasi")
def api_notifikasi():
    if "user" not in session:
        return jsonify(error="unauthorized"), 401
    items = [{"id": r["id"], "pelanggan": r["pelanggan"], "menu": r["menu"],
              "jumlah": r["jumlah"], "kapan": r["pengingat"]} for r in daftar_pengingat()]
    return jsonify(jumlah=len(items), items=items)


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
