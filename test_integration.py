import pytest

from Inventario import calcValInv, verifExis, necReab


def testInvComp():
 
    cantidad = 20
    precio = 50
    stock = 15
    cantidad_solicitada = 5
    stock_minimo = 10

    valor = calcValInv(cantidad, precio)
    existencias = verifExis(stock, cantidad_solicitada)
    reabastecimiento = necReab(stock, stock_minimo)

    assert valor == 1000
    assert existencias is True
    assert reabastecimiento is False


def testNecReab():
    cantidad = 10
    precio = 30
    stock = 3
    cantidad_solicitada = 5
    stock_minimo = 5

    valor = calcValInv(cantidad, precio)
    existencias = verifExis(stock, cantidad_solicitada)
    reabastecimiento = necReab(stock, stock_minimo)

    assert valor == 300
    assert existencias is False
    assert reabastecimiento is True


def testException():
 
    with pytest.raises(ValueError):
        valor = calcValInv(-10, 50)
        verifExis(20, 5)
        necReab(10, 5)