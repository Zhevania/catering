import pytest
from datetime import date
from logic import hitung_total, status_pengingat


def test_tanpa_diskon():
    assert hitung_total(10, 25000) == 250000


def test_diskon_otomatis_50_porsi():
    assert hitung_total(50, 20000) == 900000


def test_input_tidak_valid():
    with pytest.raises(ValueError):
        hitung_total(0, 20000)


def test_pengingat_besok():
    assert status_pengingat(date(2026, 11, 1), date(2026, 10, 31)) == "besok"


def test_pengingat_hari_ini():
    assert status_pengingat(date(2026, 10, 31), date(2026, 10, 31)) == "hari_ini"


def test_pengingat_tidak_ada():
    assert status_pengingat(date(2026, 11, 5), date(2026, 10, 31)) is None
    assert status_pengingat(None, date(2026, 10, 31)) is None