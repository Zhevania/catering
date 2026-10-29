from flask import Flask, request, redirect, render_template_string
from db import get_conn, init_db
from logic import hitung_total

app = Flask(__name__)

PAGE = """
<!doctype html><title>Catering UMKM</title>
<body style="font-family:sans-serif;max-width:800px;margin:20px auto;padding:0 12px">
<h2>🍱 Pesanan Catering UMKM</h2>
<form method="post" action="/tambah" style="display:grid;gap:6px">
 <input name="pelanggan" placeholder="Nama pelanggan" required>
 <input name="menu" placeholder="Menu (mis. Nasi Box Ayam)" required>
 <input name="jumlah" type="number" placeholder="Jumlah porsi" required>
 <input name="harga" type="number" placeholder="Harga per porsi" required>
 <input name="tanggal" type="date">
 <button>Simpan</button>
</form>
<table border="1" cellpadding="6" style="margin-top:16px;width:100%">
<tr><th>Pelanggan</th><th>Menu</th><th>Porsi</th><th>Total</th><th>Tgl</th><th>Status</th><th>Aksi</th></tr>
{% for p in data %}
<tr><td>{{p[1]}}</td><td>{{p[2]}}</td><td>{{p[3]}}</td><td>Rp{{'{:,}'.format(p[5])}}</td><td>{{p[6]}}</td><td>{{p[7]}}</td>
<td><a href="/status/{{p[0]}}">Selesai</a> | <a href="/hapus/{{p[0]}}" onclick="return confirm('Hapus?')">Hapus</a></td></tr>
{% endfor %}
</table></body>
"""

@app.route("/")
def index():
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT * FROM pesanan ORDER BY id DESC")  # READ
    data = cur.fetchall(); conn.close()
    return render_template_string(PAGE, data=data)

@app.route("/tambah", methods=["POST"])  # CREATE
def tambah():
    f = request.form
    jumlah, harga = int(f["jumlah"]), int(f["harga"])
    total = hitung_total(jumlah, harga)
    conn = get_conn(); cur = conn.cursor()
    cur.execute("INSERT INTO pesanan (pelanggan,menu,jumlah,harga_satuan,total,tanggal_acara) VALUES (%s,%s,%s,%s,%s,%s)",
                (f["pelanggan"], f["menu"], jumlah, harga, total, f["tanggal"] or None))
    conn.commit(); conn.close()
    return redirect("/")

@app.route("/status/<int:id>")  # UPDATE
def status(id):
    conn = get_conn(); cur = conn.cursor()
    cur.execute("UPDATE pesanan SET status='Selesai' WHERE id=%s", (id,))
    conn.commit(); conn.close()
    return redirect("/")

@app.route("/hapus/<int:id>")  # DELETE
def hapus(id):
    conn = get_conn(); cur = conn.cursor()
    cur.execute("DELETE FROM pesanan WHERE id=%s", (id,))
    conn.commit(); conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
