
import pytest

from Inventario import calcValInv, verifExis, necReab


def test_calcValInv():
    assert calcValInv(20, 50) == 1000


def test_invVacio():
    assert calcValInv(0, 50) == 0


def test_cantNeg():
    with pytest.raises(ValueError):
        calcValInv(-5, 50)


def test_exisSuf():
    assert verifExis(20, 5) is True


def test_exisInsuf():
    assert verifExis(3, 5) is False


def test_reabNec():
    assert necReab(5, 5) is True


def test_noReab():
    assert necReab(15, 5) is False


def test_stockNeg():
    with pytest.raises(ValueError):
        necReab(-1, 5)
