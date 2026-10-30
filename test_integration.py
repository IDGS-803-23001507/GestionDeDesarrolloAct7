import pytest

from Inventario import calcValInv, verifExis, necReab


def test_integracion_inventario_completo():
    # Datos del inventario
    cantidad = 20
    precio = 50
    stock = 15
    cantidad_solicitada = 5
    stock_minimo = 10

    # Ejecutar las funciones en conjunto
    valor = calcValInv(cantidad, precio)
    existencias = verifExis(stock, cantidad_solicitada)
    reabastecimiento = necReab(stock, stock_minimo)

    # Comprobar resultados
    assert valor == 1000
    assert existencias is True
    assert reabastecimiento is False


def test_integracion_necesidad_reabastecimiento():
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


def test_integracion_exception():
    # Comprobar que una cantidad negativa genera una excepción
    with pytest.raises(ValueError):
        valor = calcValInv(-10, 50)
        verifExis(20, 5)
        necReab(10, 5)