import pytest
from logic import hitung_total

def test_tanpa_diskon():
    assert hitung_total(10, 25000) == 250000

def test_diskon_otomatis_50_porsi():
    assert hitung_total(50, 20000) == 900000

def test_input_tidak_valid():
    with pytest.raises(ValueError):
        hitung_total(0, 20000)
