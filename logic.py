from datetime import timedelta

HARGA_PAKET = 40000     # harga per pax di dalam paket (100/200/300/500 pax)
HARGA_TAMBAHAN = 45000  # harga per 1 pax tambahan di luar pilihan paket
JUMLAH_MENU = 15        # jumlah menu yang harus dipilih per paket

# Pilihan jumlah pax di dalam paket. Harga tiap pilihan bisa diubah sendiri,
# misalnya kalau ada diskon untuk 500 pax: 500: 19000000
PILIHAN_PAX = [100, 200, 300, 500]
HARGA_PILIHAN = {p: p * HARGA_PAKET for p in PILIHAN_PAX}

# Daftar paket yang tampil di halaman pemesanan. Mau tambah paket lain?
# Tambahkan entri baru di sini (kunci, nama, deskripsi, jumlah menu yang dipilih).
PAKET = {
    "prasmanan": {
        "nama": "Paket Prasmanan",
        "deskripsi": f"Prasmanan lengkap, pilih {JUMLAH_MENU} menu favoritmu",
        "jumlah_menu": JUMLAH_MENU,
    },
}

# Daftar menu yang bisa dipilih. Ubah/tambah sesuai menu usaha kamu.
MENU_PAKET = {
    "Ayam & Daging": [
        "Ayam Rica-Rica", "Ayam Goreng Kremes", "Ayam Bakar Kecap",
        "Ayam Woku Belanga", "Rendang Sapi", "Semur Daging",
    ],
    "Ikan & Seafood": [
        "Ikan Cakalang Fufu", "Ikan Bumbu Kuning", "Udang Balado", "Cumi Goreng Tepung",
    ],
    "Sayuran": [
        "Capcay Kuah", "Tumis Kangkung", "Sayur Bunga Pepaya",
        "Oseng Buncis Wortel", "Tumis Brokoli",
    ],
    "Pendamping": [
        "Perkedel Kentang", "Tahu Isi", "Tempe Orek", "Telur Balado",
        "Bakwan Jagung", "Sambal Roa",
    ],
    "Sambal & Kerupuk": ["Sambal Dabu-Dabu", "Kerupuk Udang"],
    "Penutup": ["Puding Coklat", "Es Buah", "Buah Potong"],
}


def semua_menu():
    return [m for items in MENU_PAKET.values() for m in items]


def hitung_paket(pax_paket, pax_tambahan=0):
    """Total = harga pilihan paket (100/200/300/500 pax) + pax tambahan x Rp45.000."""
    if pax_paket not in HARGA_PILIHAN:
        raise ValueError("Pilih jumlah pax paket: " + ", ".join(map(str, PILIHAN_PAX)))
    if pax_tambahan < 0:
        raise ValueError("Pax tambahan tidak boleh negatif")
    return HARGA_PILIHAN[pax_paket] + pax_tambahan * HARGA_TAMBAHAN


def validasi_kontak(no_hp, alamat):
    """Nomor HP dan alamat wajib diisi; nomor HP dirapikan jadi angka saja."""
    hp = "".join(c for c in (no_hp or "") if c.isdigit())
    if not 9 <= len(hp) <= 15:
        raise ValueError("Nomor HP/WhatsApp tidak valid")
    if not (alamat or "").strip():
        raise ValueError("Alamat pengiriman wajib diisi")
    return hp, alamat.strip()


def hitung_dus(jumlah, harga):
    """Total pesanan dus bebas: jumlah porsi x harga per dus."""
    if jumlah <= 0:
        raise ValueError("Jumlah porsi harus lebih dari 0")
    if harga <= 0:
        raise ValueError("Harga per dus harus lebih dari 0")
    return jumlah * harga


def validasi_pilihan(pilihan, jumlah=JUMLAH_MENU):
    """Pastikan tepat `jumlah` menu berbeda dan semuanya ada di daftar."""
    unik = list(dict.fromkeys(pilihan))
    if len(unik) != jumlah:
        raise ValueError(f"Pilih tepat {jumlah} menu (sekarang {len(unik)})")
    tidak_dikenal = [m for m in unik if m not in semua_menu()]
    if tidak_dikenal:
        raise ValueError("Menu tidak dikenal: " + ", ".join(tidak_dikenal))
    return unik


def status_pengingat(tanggal_acara, hari_ini):
    """Kembalikan 'hari_ini', 'besok', atau None untuk tanggal acara."""
    if tanggal_acara is None:
        return None
    if tanggal_acara == hari_ini:
        return "hari_ini"
    if tanggal_acara == hari_ini + timedelta(days=1):
        return "besok"
    return None