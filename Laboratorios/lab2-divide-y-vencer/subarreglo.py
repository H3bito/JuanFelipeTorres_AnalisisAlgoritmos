def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """
    Encuentra el subarreglo contiguo de suma máxima mediante fuerza bruta.

    Retorna:
        (indice_inicio, indice_fin, suma_maxima)

    Los índices son inclusivos.
    """
    n = len(valores)

    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = float("-inf")

    for inicio in range(n):
        suma_actual = 0

        for fin in range(inicio, n):
            suma_actual += valores[fin]

            if suma_actual > mejor_suma:
                mejor_suma = suma_actual
                mejor_inicio = inicio
                mejor_fin = fin

    return mejor_inicio, mejor_fin, mejor_suma


def suma_cruzada(
    valores: list[float],
    inicio: int,
    medio: int,
    fin: int
) -> tuple[int, int, float]:
    """
    Encuentra el mejor subarreglo que cruza el punto medio.
    Los extremos inicio y fin son inclusivos.
    """
    suma_actual = 0
    mejor_suma_izquierda = float("-inf")
    mejor_inicio = medio

    for i in range(medio, inicio - 1, -1):
        suma_actual += valores[i]

        if suma_actual > mejor_suma_izquierda:
            mejor_suma_izquierda = suma_actual
            mejor_inicio = i

    suma_actual = 0
    mejor_suma_derecha = float("-inf")
    mejor_fin = medio + 1

    for j in range(medio + 1, fin + 1):
        suma_actual += valores[j]

        if suma_actual > mejor_suma_derecha:
            mejor_suma_derecha = suma_actual
            mejor_fin = j

    return (
        mejor_inicio,
        mejor_fin,
        mejor_suma_izquierda + mejor_suma_derecha
    )


def subarreglo_maximo(
    valores: list[float],
    inicio: int,
    fin: int
) -> tuple[int, int, float]:
    """
    Encuentra el subarreglo de suma máxima mediante dividir y vencer.
    Los índices inicio y fin son inclusivos.
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    izq_inicio, izq_fin, suma_izquierda = subarreglo_maximo(
        valores, inicio, medio
    )

    der_inicio, der_fin, suma_derecha = subarreglo_maximo(
        valores, medio + 1, fin
    )

    cruz_inicio, cruz_fin, suma_cruce = suma_cruzada(
        valores, inicio, medio, fin
    )

    if suma_izquierda >= suma_derecha and suma_izquierda >= suma_cruce:
        return izq_inicio, izq_fin, suma_izquierda

    if suma_derecha >= suma_izquierda and suma_derecha >= suma_cruce:
        return der_inicio, der_fin, suma_derecha

    return cruz_inicio, cruz_fin, suma_cruce