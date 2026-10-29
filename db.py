import os
import mysql.connector
from werkzeug.security import generate_password_hash


def _cfg(with_db=True):
    cfg = dict(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASS", ""),
    )
    if with_db:
        cfg["database"] = os.getenv("DB_NAME", "catering_umkm")
    return cfg


def get_conn():
    return mysql.connector.connect(**_cfg())


def init_db():
    conn = mysql.connector.connect(**_cfg(with_db=False))
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS catering_umkm")
    cur.execute("USE catering_umkm")
    cur.execute("""CREATE TABLE IF NOT EXISTS pesanan (
        id INT AUTO_INCREMENT PRIMARY KEY,
        pelanggan VARCHAR(100) NOT NULL,
        menu VARCHAR(100) NOT NULL,
        jumlah INT NOT NULL,
        harga_satuan INT NOT NULL,
        total INT NOT NULL,
        tanggal_acara DATE,
        status VARCHAR(20) DEFAULT 'Baru'
    )""")
    # Tambah kolom baru kalau tabel lama belum punya (aman dijalankan berulang)
    cur.execute("SELECT COLUMN_NAME FROM information_schema.COLUMNS "
                "WHERE TABLE_SCHEMA='catering_umkm' AND TABLE_NAME='pesanan'")
    kolom = {str(r[0]).lower() for r in cur.fetchall()}
    if "jenis" not in kolom:
        cur.execute("ALTER TABLE pesanan ADD COLUMN jenis VARCHAR(10) NOT NULL DEFAULT 'Dus'")
    if "pilihan_menu" not in kolom:
        cur.execute("ALTER TABLE pesanan ADD COLUMN pilihan_menu TEXT NULL")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL
    )""")
    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        cur.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (os.getenv("ADMIN_USER", "admin"),
             generate_password_hash(os.getenv("ADMIN_PASS", "admin123"))),
        )
    conn.commit()
    conn.close()