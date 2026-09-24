"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = datos.copy()
    comparaciones = 0

    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if lista[j] < clave:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break

        lista[j + 1] = clave

    return lista, comparaciones

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = datos.copy()

    def dividir_y_ordenar(lista_actual: list[int]) -> tuple[list[int], int]:
        if len(lista_actual) <= 1:
            return lista_actual, 0

        mitad = len(lista_actual) // 2

        izquierda, comparaciones_izquierda = dividir_y_ordenar(
            lista_actual[:mitad]
        )
        derecha, comparaciones_derecha = dividir_y_ordenar(
            lista_actual[mitad:]
        )

        resultado = []
        i = 0
        j = 0
        comparaciones_mezcla = 0

        while i < len(izquierda) and j < len(derecha):
            comparaciones_mezcla += 1

            if izquierda[i] >= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        comparaciones_totales = (
            comparaciones_izquierda
            + comparaciones_derecha
            + comparaciones_mezcla
        )

        return resultado, comparaciones_totales

    return dividir_y_ordenar(lista)