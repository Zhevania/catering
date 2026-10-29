from datetime import timedelta

HARGA_PAKET = 40000   # per pax
MIN_PAX = 50          # minimal pemesanan paket
JUMLAH_MENU = 15      # jumlah menu yang harus dipilih per paket

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


def hitung_paket(pax):
    """Total paket prasmanan: pax x Rp40.000, minimal 50 pax."""
    if pax < MIN_PAX:
        raise ValueError(f"Pemesanan paket minimal {MIN_PAX} pax")
    return pax * HARGA_PAKET


def hitung_dus(jumlah, harga):
    """Total pesanan dus bebas: jumlah porsi x harga per dus."""
    if jumlah <= 0:
        raise ValueError("Jumlah porsi harus lebih dari 0")
    if harga <= 0:
        raise ValueError("Harga per dus harus lebih dari 0")
    return jumlah * harga


def validasi_pilihan(pilihan):
    """Pastikan tepat 15 menu berbeda dan semuanya ada di daftar."""
    unik = list(dict.fromkeys(pilihan))
    if len(unik) != JUMLAH_MENU:
        raise ValueError(f"Pilih tepat {JUMLAH_MENU} menu (sekarang {len(unik)})")
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