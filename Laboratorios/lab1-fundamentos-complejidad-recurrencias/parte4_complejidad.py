"""Comparacion de insertion sort y merge sort."""

import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3


def medir_algoritmo(algoritmo, datos: list[int]) -> float:
    """Mide el tiempo promedio de ejecucion de un algoritmo."""
    tiempos = []

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        algoritmo(datos)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return sum(tiempos) / REPETICIONES


def ejecutar_experimento():
    """Compara los tiempos de ambos algoritmos."""
    resultados = {
        "Insertion sort": [],
        "Merge sort": [],
    }

    for n in TAMANOS:
        datos = generar_aleatorio(n)

        tiempo_insertion = medir_algoritmo(insertion_sort, datos)
        tiempo_merge = medir_algoritmo(merge_sort, datos)

        resultados["Insertion sort"].append(tiempo_insertion)
        resultados["Merge sort"].append(tiempo_merge)

        print(f"\nTamaño de entrada: {n}")
        print(f"Insertion sort | tiempo: {tiempo_insertion:.6f} s")
        print(f"Merge sort     | tiempo: {tiempo_merge:.6f} s")

    return resultados


def graficar_tiempos(resultados):
    """Genera la grafica comparativa de tiempos."""
    plt.figure()

    for nombre, tiempos in resultados.items():
        plt.plot(
            TAMANOS,
            tiempos,
            marker="o",
            label=nombre,
        )

    plt.title("Comparacion de insertion sort y merge sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()


def main():
    """Ejecuta el experimento y genera la grafica."""
    resultados = ejecutar_experimento()

    graficar_tiempos(resultados)

    print("\nExperimento terminado.")
    print("Grafica guardada en la carpeta 'graficas'.")


if __name__ == "__main__":
    main()