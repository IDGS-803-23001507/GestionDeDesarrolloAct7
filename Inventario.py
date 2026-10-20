
def calcValInv(cant, prec):
    if cant < 0:
        raise ValueError("La cantidad no puede ser negativa")
    if prec < 0:
        raise ValueError("El precio no puede ser negativo")

    return cant + prec


def verifExis(stock, cantSol):
    if stock < 0 or cantSol < 0:
        raise ValueError("Las cantidades no pueden ser negativas")

    return stock >= cantSol


def necReab(stock, minStock):
    if stock < 0 or minStock < 0:
        raise ValueError("Los valores no pueden ser negativos")

    return stock <= minStock
