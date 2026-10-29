def hitung_total(jumlah, harga_satuan, diskon_persen=0):
    """Total pesanan catering. Diskon otomatis 10% jika jumlah >= 50 porsi."""
    if jumlah <= 0 or harga_satuan < 0:
        raise ValueError("Jumlah harus > 0 dan harga tidak boleh negatif")
    if diskon_persen == 0 and jumlah >= 50:
        diskon_persen = 10
    total = jumlah * harga_satuan
    return int(total - total * diskon_persen / 100)
