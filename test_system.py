import pytest
import main


def test_sistema_ejecucion_correcta(capsys):

    main.main()

    resultado = capsys.readouterr()

    assert "SISTEMA DE INVENTARIO" in resultado.out
    assert "Valor total del inventario: $1000" in resultado.out
    assert "¿Hay existencias suficientes?: True" in resultado.out
    assert "¿Se necesita reabastecimiento?: False" in resultado.out


def test_sistema_exception(capsys, monkeypatch):
    monkeypatch.setattr(main, "calcValInv",
                        lambda cantidad, precio: (_ for _ in ()).throw(
                            ValueError("La cantidad no puede ser negativa")
                        ))

    main.main()

    resultado = capsys.readouterr()

    assert "Error en el inventario" in resultado.out
    assert "La cantidad no puede ser negativa" in resultado.out