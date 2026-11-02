import pytest
from datetime import date
from logic import (hitung_paket, hitung_dus, validasi_pilihan, validasi_kontak,
                   semua_menu, status_pengingat, JUMLAH_MENU)


def test_paket_pilihan_pax():
    assert hitung_paket(100) == 4000000
    assert hitung_paket(200) == 8000000
    assert hitung_paket(300) == 12000000
    assert hitung_paket(500) == 20000000


def test_paket_dengan_pax_tambahan():
    assert hitung_paket(100, 10) == 4000000 + 10 * 45000
    assert hitung_paket(500, 1) == 20000000 + 45000


def test_paket_pax_tidak_valid():
    with pytest.raises(ValueError):
        hitung_paket(150)
    with pytest.raises(ValueError):
        hitung_paket(100, -1)


def test_kontak():
    assert validasi_kontak("0812-3456-7890", " Jl. Mawar 1 ") == ("081234567890", "Jl. Mawar 1")
    with pytest.raises(ValueError):
        validasi_kontak("123", "Jl. Mawar")
    with pytest.raises(ValueError):
        validasi_kontak("081234567890", "  ")


def test_dus_bebas():
    assert hitung_dus(12, 18500) == 222000


def test_dus_tidak_valid():
    with pytest.raises(ValueError):
        hitung_dus(0, 10000)
    with pytest.raises(ValueError):
        hitung_dus(5, 0)


def test_pilihan_menu_15():
    assert len(validasi_pilihan(semua_menu()[:JUMLAH_MENU])) == JUMLAH_MENU


def test_pilihan_menu_kurang_atau_lebih():
    with pytest.raises(ValueError):
        validasi_pilihan(semua_menu()[:14])
    with pytest.raises(ValueError):
        validasi_pilihan(semua_menu()[:16])


def test_pilihan_menu_tidak_dikenal():
    daftar = semua_menu()[:14] + ["Menu Palsu"]
    with pytest.raises(ValueError):
        validasi_pilihan(daftar)


def test_pengingat():
    assert status_pengingat(date(2026, 11, 1), date(2026, 10, 31)) == "besok"
    assert status_pengingat(date(2026, 10, 31), date(2026, 10, 31)) == "hari_ini"
    assert status_pengingat(date(2026, 11, 5), date(2026, 10, 31)) is None
    assert status_pengingat(None, date(2026, 10, 31)) is None