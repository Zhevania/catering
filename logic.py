import re
import secrets
from datetime import date, timedelta

MIN_HARI_PESAN = 3   # pembeli minimal pesan 3 hari sebelum acara

# Paket untuk pembeli. Ubah nama, pax, harga, deskripsi, jumlah menu, dan daftar menu di sini.
# "harga" = harga per pax. "jumlah_menu" = berapa menu yang harus dipilih dari daftar "menu".
_DASAR = ["Nasi Putih", "Nasi Kuning", "Ayam Bakar Madu", "Ayam Goreng Kremes",
          "Telur Balado", "Tumis Buncis", "Sambal Terong", "Kerupuk & Sambal"]
_TENGAH = _DASAR + ["Rendang Sapi", "Ikan Bakar Rica", "Capcay Kuah"]
_ATAS = _TENGAH + ["Cumi Saus Padang", "Puding Coklat", "Es Buah"]

PAKET = {
    "hemat": {
        "nama": "Paket Hemat", "pax": 25, "harga": 45000,
        "deskripsi": "Cocok untuk arisan dan acara keluarga kecil",
        "jumlah_menu": 4, "menu": _DASAR,
    },
    "standar": {
        "nama": "Paket Standar", "pax": 50, "harga": 50000,
        "deskripsi": "Pilihan favorit untuk syukuran dan rapat",
        "jumlah_menu": 5, "menu": _TENGAH,
    },
    "premium": {
        "nama": "Paket Premium", "pax": 100, "harga": 55000,
        "deskripsi": "Untuk pernikahan kecil dan acara kantor",
        "jumlah_menu": 6, "menu": _ATAS,
    },
}


def paket_by_nama(nama):
    """Cari kode paket dari nama paket (untuk membuka pesanan di halaman edit)."""
    for kode, p in PAKET.items():
        if p["nama"] == nama:
            return kode
    return ""


def hitung_paket(kode):
    """Total paket = pax x harga per pax."""
    p = PAKET.get(kode)
    if not p:
        raise ValueError("Pilih salah satu paket yang tersedia")
    return p["pax"] * p["harga"]


def validasi_pilihan(kode, pilihan):
    """Pastikan jumlah menu sesuai paket dan semuanya ada di daftar menu paket itu."""
    p = PAKET.get(kode)
    if not p:
        raise ValueError("Pilih salah satu paket yang tersedia")
    unik = list(dict.fromkeys(pilihan))
    if len(unik) != p["jumlah_menu"]:
        raise ValueError(f"Pilih tepat {p['jumlah_menu']} menu untuk {p['nama']} (sekarang {len(unik)})")
    di_luar = [m for m in unik if m not in p["menu"]]
    if di_luar:
        raise ValueError("Menu tidak tersedia di paket ini: " + ", ".join(di_luar))
    return unik


def hitung_dus(jumlah, harga):
    """Total pesanan dus bebas (admin): jumlah porsi x harga per dus."""
    if jumlah <= 0:
        raise ValueError("Jumlah porsi harus lebih dari 0")
    if harga <= 0:
        raise ValueError("Harga per dus harus lebih dari 0")
    return jumlah * harga


def validasi_tanggal(teks, hari_ini, min_hari=MIN_HARI_PESAN):
    """Ubah teks YYYY-MM-DD menjadi date, dan pastikan tidak terlalu dekat."""
    try:
        tgl = date.fromisoformat((teks or "").strip())
    except ValueError:
        raise ValueError("Tanggal acara wajib diisi dengan benar")
    if tgl < hari_ini + timedelta(days=min_hari):
        raise ValueError(f"Pemesanan minimal {min_hari} hari sebelum acara")
    return tgl


def validasi_jam(teks):
    """Jam acara opsional, format HH:MM. Kosong -> None."""
    teks = (teks or "").strip()
    if not teks:
        return None
    if not re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", teks):
        raise ValueError("Format jam acara tidak valid")
    return teks


def buat_kode():
    """Kode pesanan acak, mis. QC-7F3K9Q."""
    abjad = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return "QC-" + "".join(secrets.choice(abjad) for _ in range(6))


def status_pengingat(tanggal_acara, hari_ini):
    """Kembalikan 'hari_ini', 'besok', atau None untuk tanggal acara."""
    if tanggal_acara is None:
        return None
    if tanggal_acara == hari_ini:
        return "hari_ini"
    if tanggal_acara == hari_ini + timedelta(days=1):
        return "besok"
    return None


def normalisasi_nomor(nomor):
    """Ubah 0812..., 812..., +62812... menjadi 62812... (format WhatsApp)."""
    digit = re.sub(r"\D", "", nomor or "")
    if digit.startswith("0"):
        digit = "62" + digit[1:]
    elif digit.startswith("8"):
        digit = "62" + digit
    if not digit.startswith("62") or not (10 <= len(digit) <= 15):
        raise ValueError("Nomor WhatsApp tidak valid. Contoh: 081234567890")
    return digit