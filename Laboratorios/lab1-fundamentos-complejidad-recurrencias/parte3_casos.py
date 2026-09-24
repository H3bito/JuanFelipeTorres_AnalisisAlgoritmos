"""Experimento de peor, mejor y caso promedio para insertion sort."""

import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3


def medir_insertion_sort(generador, n: int) -> tuple[float, int]:
    """Mide el tiempo y las comparaciones de insertion sort.

    Args:
        generador: funcion que genera los datos de entrada.
        n: cantidad de elementos de la entrada.

    Returns:
        Una tupla con el tiempo promedio en segundos y las
        comparaciones realizadas.
    """
    datos = generador(n)

    tiempos = []
    comparaciones = 0

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    tiempo_promedio = sum(tiempos) / REPETICIONES

    return tiempo_promedio, comparaciones


def ejecutar_experimento():
    """Ejecuta las mediciones para los tres escenarios."""
    escenarios = {
        "Aleatorio": generar_aleatorio,
        "Casi ordenado": generar_casi_ordenado,
        "Inverso": generar_inverso,
    }

    resultados = {
        nombre: {
            "tiempos": [],
            "comparaciones": [],
        }
        for nombre in escenarios
    }

    for n in TAMANOS:
        print(f"\nTamaño de entrada: {n}")

        for nombre, generador in escenarios.items():
            tiempo, comparaciones = medir_insertion_sort(generador, n)

            resultados[nombre]["tiempos"].append(tiempo)
            resultados[nombre]["comparaciones"].append(comparaciones)

            print(
                f"{nombre:16} | "
                f"tiempo: {tiempo:.6f} s | "
                f"comparaciones: {comparaciones}"
            )

    return resultados


def graficar_comparaciones(resultados):
    """Genera la grafica de comparaciones frente al tamaño."""
    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["comparaciones"],
            marker="o",
            label=nombre,
        )

    plt.title("Insertion sort: comparaciones vs. tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()


def graficar_tiempos(resultados):
    """Genera la grafica de tiempo frente al tamaño."""
    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["tiempos"],
            marker="o",
            label=nombre,
        )

    plt.title("Insertion sort: tiempo vs. tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()


def main():
    """Ejecuta el experimento y genera las graficas."""
    resultados = ejecutar_experimento()

    graficar_comparaciones(resultados)
    graficar_tiempos(resultados)

    print("\nExperimento terminado.")
    print("Graficas guardadas en la carpeta 'graficas'.")


if __name__ == "__main__":
    main()