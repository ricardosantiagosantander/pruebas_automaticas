import pytest
from app.calculos import sumar, dividir ,multiplicar


def test_sumar():
    assert sumar(2, 3) == 5


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_para_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_miltiplciar():
    assert multiplicar(2,10)==20