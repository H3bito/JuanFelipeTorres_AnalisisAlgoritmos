import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def ejecutar_pruebas():
    # 1. Ejemplo principal del laboratorio.
    valores = [-3, 5, -2, 8, -6, 3, 9, -4]

    inicio, fin, suma = subarreglo_fuerza_bruta(valores)
    assert suma == 17, f"Fuerza bruta falló: {suma}"

    inicio, fin, suma = subarreglo_maximo(valores, 0, len(valores) - 1)
    assert suma == 17, f"Dividir y vencer falló: {suma}"

    # 2. Lista con un solo elemento.
    valores = [7]

    assert subarreglo_fuerza_bruta(valores)[2] == 7
    assert subarreglo_maximo(valores, 0, 0)[2] == 7

    # 3. Todos los elementos son negativos.
    valores = [-8, -2, -5]

    assert subarreglo_fuerza_bruta(valores)[2] == -2
    assert subarreglo_maximo(valores, 0, 2)[2] == -2

    # 4. Todos los elementos son positivos.
    valores = [1, 2, 3, 4]

    assert subarreglo_fuerza_bruta(valores)[2] == 10
    assert subarreglo_maximo(valores, 0, 3)[2] == 10

    # 5. El mejor subarreglo cruza el punto medio.
    valores = [4, -1, 2, -1, 5]

    assert subarreglo_fuerza_bruta(valores)[2] == 9
    assert subarreglo_maximo(valores, 0, 4)[2] == 9

    # 6. Comparación con 20 listas aleatorias.
    random.seed(42)

    for caso in range(20):
        longitud = random.randint(1, 30)
        valores = [
            random.randint(-20, 20)
            for _ in range(longitud)
        ]

        suma_fuerza_bruta = subarreglo_fuerza_bruta(valores)[2]
        suma_dividir_vencer = subarreglo_maximo(
            valores, 0, len(valores) - 1
        )[2]

        assert suma_fuerza_bruta == suma_dividir_vencer, (
            f"Error en el caso aleatorio {caso + 1}: "
            f"lista={valores}, "
            f"fuerza bruta={suma_fuerza_bruta}, "
            f"dividir y vencer={suma_dividir_vencer}"
        )

    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()