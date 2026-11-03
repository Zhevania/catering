import re
import pytest
from datetime import date
from logic import (PAKET, paket_by_nama, hitung_paket, hitung_dus, validasi_pilihan,
                   validasi_tanggal, validasi_jam, buat_kode, status_pengingat,
                   normalisasi_nomor)


def test_harga_paket():
    assert hitung_paket("hemat") == 1125000
    assert hitung_paket("standar") == 2500000
    assert hitung_paket("premium") == 5500000


def test_paket_tidak_ada():
    with pytest.raises(ValueError):
        hitung_paket("super")


def test_paket_by_nama():
    assert paket_by_nama("Paket Standar") == "standar"
    assert paket_by_nama("Paket Lama") == ""


def test_pilihan_menu_sesuai_paket():
    for kode, p in PAKET.items():
        assert len(validasi_pilihan(kode, p["menu"][:p["jumlah_menu"]])) == p["jumlah_menu"]


def test_pilihan_menu_jumlah_salah():
    menu = PAKET["hemat"]["menu"]
    with pytest.raises(ValueError):
        validasi_pilihan("hemat", menu[:3])
    with pytest.raises(ValueError):
        validasi_pilihan("hemat", menu[:5])


def test_pilihan_menu_di_luar_paket():
    pilihan = PAKET["hemat"]["menu"][:3] + ["Es Buah"]   # Es Buah hanya ada di Premium
    with pytest.raises(ValueError):
        validasi_pilihan("hemat", pilihan)


def test_dus_bebas():
    assert hitung_dus(12, 18500) == 222000
    with pytest.raises(ValueError):
        hitung_dus(0, 10000)
    with pytest.raises(ValueError):
        hitung_dus(5, 0)


def test_validasi_tanggal():
    hari = date(2026, 11, 2)
    assert validasi_tanggal("2026-11-05", hari) == date(2026, 11, 5)
    with pytest.raises(ValueError):
        validasi_tanggal("2026-11-04", hari)
    with pytest.raises(ValueError):
        validasi_tanggal("bukan tanggal", hari)


def test_validasi_jam():
    assert validasi_jam("") is None
    assert validasi_jam("09:30") == "09:30"
    with pytest.raises(ValueError):
        validasi_jam("25:00")


def test_kode_pesanan():
    assert re.fullmatch(r"QC-[A-Z2-9]{6}", buat_kode())


def test_pengingat():
    assert status_pengingat(date(2026, 11, 1), date(2026, 10, 31)) == "besok"
    assert status_pengingat(date(2026, 10, 31), date(2026, 10, 31)) == "hari_ini"
    assert status_pengingat(date(2026, 11, 5), date(2026, 10, 31)) is None
    assert status_pengingat(None, date(2026, 10, 31)) is None


def test_normalisasi_nomor():
    assert normalisasi_nomor("0812-3456-7890") == "6281234567890"
    assert normalisasi_nomor("+62 812 3456 7890") == "6281234567890"
    assert normalisasi_nomor("81234567890") == "6281234567890"
    with pytest.raises(ValueError):
        normalisasi_nomor("123")