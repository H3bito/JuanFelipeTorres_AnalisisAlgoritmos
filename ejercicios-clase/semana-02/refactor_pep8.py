def calcular_promedio(lista: list[int]) -> float:
    """Calcula el promedio de una lista de números.

    Args:
        lista: Lista de números enteros.

    Returns:
        El promedio de los números.
    """
    suma = 0

    for numero in lista:
        suma = suma + numero

    return suma / len(lista)


def main() -> None:
    """Punto de entrada del programa."""
    lista = [1, 2, 3, 4, 5]
    print(calcular_promedio(lista))


if __name__ == "__main__":
    main()