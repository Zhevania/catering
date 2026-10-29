import pytest
from datetime import date
from logic import (hitung_paket, hitung_dus, validasi_pilihan, semua_menu,
                   status_pengingat, JUMLAH_MENU)


def test_paket_50_pax():
    assert hitung_paket(50) == 2000000


def test_paket_di_bawah_minimal():
    with pytest.raises(ValueError):
        hitung_paket(49)


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