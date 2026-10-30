from Inventario import calcValInv, verifExis, necReab


def main():
    print("===== SISTEMA DE INVENTARIO =====")

    try:
        # Datos del inventario
        cantidad = 20
        precio = 50
        stock = 15
        cantidad_solicitada = 5
        stock_minimo = 10

        # Calcular valor del inventario
        valor = calcValInv(cantidad, precio)
        print(f"Valor total del inventario: ${valor}")

        # Verificar existencias
        existe = verifExis(stock, cantidad_solicitada)
        print(f"¿Hay existencias suficientes?: {existe}")

        # Verificar necesidad de reabastecimiento
        reabastecer = necReab(stock, stock_minimo)
        print(f"¿Se necesita reabastecimiento?: {reabastecer}")

    except ValueError as error:
        print(f"Error en el inventario: {error}")

    except Exception as error:
        print(f"Error inesperado: {error}")


if __name__ == "__main__":
    main()