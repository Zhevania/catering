import os
import mysql.connector

def get_conn():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASS", ""),
        database=os.getenv("DB_NAME", "catering_umkm"),
    )

def init_db():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASS", ""),
    )
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
    conn.commit(); conn.close()
