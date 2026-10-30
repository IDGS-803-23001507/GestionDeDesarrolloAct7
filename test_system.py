import pytest
import main


def test_sistema_ejecucion_correcta(capsys):
    # Ejecutar el programa principal
    main.main()

    # Capturar lo que imprime el programa
    resultado = capsys.readouterr()

    # Comprobar los resultados
    assert "SISTEMA DE INVENTARIO" in resultado.out
    assert "Valor total del inventario: $1000" in resultado.out
    assert "¿Hay existencias suficientes?: True" in resultado.out
    assert "¿Se necesita reabastecimiento?: False" in resultado.out


def test_sistema_exception(capsys, monkeypatch):
    # Simular una cantidad negativa para provocar ValueError
    monkeypatch.setattr(main, "calcValInv",
                        lambda cantidad, precio: (_ for _ in ()).throw(
                            ValueError("La cantidad no puede ser negativa")
                        ))

    # Ejecutar el programa
    main.main()

    # Capturar el resultado
    resultado = capsys.readouterr()

    # Comprobar que el error fue capturado
    assert "Error en el inventario" in resultado.out
    assert "La cantidad no puede ser negativa" in resultado.out