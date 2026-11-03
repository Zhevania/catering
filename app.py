import os
from datetime import datetime, timedelta, timezone
from functools import wraps

from flask import (Flask, request, redirect, url_for, session, flash,
                   render_template, jsonify)
from jinja2 import DictLoader
from werkzeug.security import check_password_hash

from db import get_conn, init_db
from logic import (PAKET, MIN_HARI_PESAN, paket_by_nama, hitung_paket, hitung_dus,
                   validasi_pilihan, validasi_tanggal, validasi_jam, buat_kode,
                   status_pengingat, normalisasi_nomor)
from templates import TEMPLATES

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "catering-umkm-dev-key")
app.jinja_loader = DictLoader(TEMPLATES)
MIN_HARI = int(os.getenv("MIN_HARI_PESAN", MIN_HARI_PESAN))
app.jinja_env.globals.update(PAKET=PAKET, MIN_HARI=MIN_HARI)

TZ = timezone(timedelta(hours=int(os.getenv("TZ_OFFSET", "8"))))  # WITA
BULAN = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]


@app.template_filter("rupiah")
def rupiah(n):
    return "Rp " + f"{int(n or 0):,}".replace(",", ".")


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


def _extra(f):
    """Data tambahan pembeli (opsional) saat admin mengedit pesanan."""
    tel = f.get("telepon", "").strip()
    tel = normalisasi_nomor(tel) if tel else None
    return (tel, f.get("alamat", "").strip() or None,
            f.get("catatan", "").strip() or None, validasi_jam(f.get("jam", "")))


# =====================================================
#                  HALAMAN PEMBELI
# =====================================================
def _halaman_pembeli(form=None, error=None):
    form = form if form is not None else {}
    terpilih = form.getlist("menu") if hasattr(form, "getlist") else []
    min_tgl = (hari_ini() + timedelta(days=MIN_HARI)).isoformat()
    return render_template("beranda.html", f=form, terpilih=terpilih, error=error, min_tgl=min_tgl)


@app.route("/")
def beranda():
    return _halaman_pembeli()


@app.route("/pesan", methods=["POST"])
def pesan():
    f = request.form
    if f.get("website"):  # jebakan spam (kolom tersembunyi)
        return redirect(url_for("beranda"))
    try:
        kp = f.get("paket", "")
        total = hitung_paket(kp)
        pilihan = validasi_pilihan(kp, f.getlist("menu"))
        paket = PAKET[kp]
        nama = _nama(f)
        telepon = normalisasi_nomor(f.get("telepon", ""))
        alamat = f.get("alamat", "").strip()
        if not alamat:
            raise ValueError("Alamat / lokasi acara wajib diisi")
        tanggal = validasi_tanggal(f.get("tanggal", ""), hari_ini(), MIN_HARI)
        jam = validasi_jam(f.get("jam", ""))
        catatan = f.get("catatan", "").strip()[:500] or None
    except ValueError as e:
        return _halaman_pembeli(f, str(e)), 400

    kode = buat_kode()
    for _ in range(5):
        if not query("SELECT 1 AS x FROM pesanan WHERE kode=%s", (kode,), one=True):
            break
        kode = buat_kode()
    query("INSERT INTO pesanan (pelanggan,menu,jumlah,harga_satuan,total,tanggal_acara,jenis,"
          "pilihan_menu,telepon,alamat,catatan,jam_acara,sumber,kode) "
          "VALUES (%s,%s,%s,%s,%s,%s,'Paket',%s,%s,%s,%s,%s,'Online',%s)",
          (nama, paket["nama"], paket["pax"], paket["harga"], total, tanggal,
           "|".join(pilihan), telepon, alamat, catatan, jam, kode), commit=True)
    flash("Pesanan berhasil dikirim", "ok")
    return redirect(url_for("lihat_pesanan", kode=kode))


@app.route("/pesanan/<kode>")
def lihat_pesanan(kode):
    p = query("SELECT * FROM pesanan WHERE kode=%s", (kode.strip().upper(),), one=True)
    if not p:
        flash("Kode pesanan tidak ditemukan", "error")
        return redirect(url_for("beranda"))
    return render_template("pesanan.html", p=p)


@app.route("/cek")
def cek_pesanan():
    kode = request.args.get("kode", "").strip().upper()
    if not kode:
        return redirect(url_for("beranda"))
    return redirect(url_for("lihat_pesanan", kode=kode))


# =====================================================
#                  HALAMAN ADMIN
# =====================================================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = query("SELECT * FROM users WHERE username=%s",
                  (request.form.get("username", "").strip(),), one=True)
        if u and check_password_hash(u["password_hash"], request.form.get("password", "")):
            session["user"] = u["username"]
            return redirect(url_for("admin"))
        flash("Username atau password salah", "error")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("beranda"))


@app.route("/admin")
@login_required
def admin():
    q = request.args.get("q", "").strip()
    st = request.args.get("status", "")
    sql, params = "SELECT * FROM pesanan WHERE 1=1", []
    if q:
        sql += " AND (pelanggan LIKE %s OR menu LIKE %s OR kode LIKE %s OR telepon LIKE %s)"
        params += [f"%{q}%"] * 4
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


@app.route("/tambah_paket", methods=["POST"])
@login_required
def tambah_paket():
    try:
        f = request.form
        nama = _nama(f)
        kp = f.get("paket", "")
        total = hitung_paket(kp)
        pilihan = validasi_pilihan(kp, f.getlist("menu"))
        paket = PAKET[kp]
        query("INSERT INTO pesanan (pelanggan,menu,jumlah,harga_satuan,total,tanggal_acara,jenis,pilihan_menu) "
              "VALUES (%s,%s,%s,%s,%s,%s,'Paket',%s)",
              (nama, paket["nama"], paket["pax"], paket["harga"], total,
               f.get("tanggal") or None, "|".join(pilihan)), commit=True)
        flash("Pesanan paket berhasil ditambahkan", "ok")
    except (ValueError, KeyError) as e:
        flash(f"Gagal: {e}", "error")
    return redirect(url_for("admin"))


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
    return redirect(url_for("admin"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    p = query("SELECT * FROM pesanan WHERE id=%s", (id,), one=True)
    if not p:
        flash("Pesanan tidak ditemukan", "error")
        return redirect(url_for("admin"))
    if request.method == "POST":
        try:
            f = request.form
            nama, tanggal = _nama(f), f.get("tanggal") or None
            tel, alamat, catatan, jam = _extra(f)
            if p["jenis"] == "Paket":
                kp = f.get("paket", "")
                total = hitung_paket(kp)
                pilihan = validasi_pilihan(kp, f.getlist("menu"))
                paket = PAKET[kp]
                query("UPDATE pesanan SET pelanggan=%s, menu=%s, jumlah=%s, harga_satuan=%s, total=%s, "
                      "tanggal_acara=%s, pilihan_menu=%s, telepon=%s, alamat=%s, catatan=%s, jam_acara=%s "
                      "WHERE id=%s",
                      (nama, paket["nama"], paket["pax"], paket["harga"], total, tanggal,
                       "|".join(pilihan), tel, alamat, catatan, jam, id), commit=True)
            else:
                menu = f.get("menu", "").strip()
                if not menu:
                    raise ValueError("Nama menu dus wajib diisi")
                jumlah, harga = int(f["jumlah"]), int(f["harga"])
                total = hitung_dus(jumlah, harga)
                query("UPDATE pesanan SET pelanggan=%s, menu=%s, jumlah=%s, harga_satuan=%s, total=%s, "
                      "tanggal_acara=%s, telepon=%s, alamat=%s, catatan=%s, jam_acara=%s WHERE id=%s",
                      (nama, menu, jumlah, harga, total, tanggal, tel, alamat, catatan, jam, id),
                      commit=True)
            flash("Pesanan berhasil diperbarui", "ok")
            return redirect(url_for("admin"))
        except (ValueError, KeyError) as e:
            flash(f"Gagal: {e}", "error")
    return render_template("edit.html", p=p, user=session["user"],
                           paket_key=paket_by_nama(p["menu"]) if p["jenis"] == "Paket" else "")


@app.route("/status/<int:id>", methods=["POST"])
@login_required
def status(id):
    query("UPDATE pesanan SET status='Selesai' WHERE id=%s", (id,), commit=True)
    flash("Pesanan ditandai selesai", "ok")
    return redirect(request.referrer or url_for("admin"))


@app.route("/hapus/<int:id>", methods=["POST"])
@login_required
def hapus(id):
    query("DELETE FROM pesanan WHERE id=%s", (id,), commit=True)
    flash("Pesanan dihapus", "ok")
    return redirect(url_for("admin"))


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