import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def medir_tiempo(funcion, *argumentos):
    """Mide únicamente el tiempo de ejecución de la función."""
    inicio = time.perf_counter()
    resultado = funcion(*argumentos)
    fin = time.perf_counter()

    return resultado, fin - inicio


def ejecutar_mediciones():
    # Tamaños de entrada: ocho mediciones, desde listas pequeñas
    # hasta una lista de 8000 elementos.
    tamanos = [10, 50, 100, 500, 1000, 2000, 4000, 8000]

    # Semilla fija para que los datos sean reproducibles.
    generador = random.Random(42)

    tiempos_fuerza_bruta = []
    tiempos_dividir_vencer = []

    for n in tamanos:
        valores = [
            generador.randint(-100, 100)
            for _ in range(n)
        ]

        # Repetimos cada medición tres veces para reducir
        # el efecto de variaciones puntuales del sistema.
        mediciones_fb = []
        mediciones_dv = []

        for _ in range(3):
            resultado_fb, tiempo_fb = medir_tiempo(
                subarreglo_fuerza_bruta, valores
            )

            resultado_dv, tiempo_dv = medir_tiempo(
                subarreglo_maximo, valores, 0, len(valores) - 1
            )

            # Verificamos que ambos algoritmos den la misma suma.
            assert resultado_fb[2] == resultado_dv[2], (
                f"Los resultados no coinciden para n={n}"
            )

            mediciones_fb.append(tiempo_fb)
            mediciones_dv.append(tiempo_dv)

        # Usamos la mediana de las tres mediciones.
        tiempo_fb = statistics.median(mediciones_fb)
        tiempo_dv = statistics.median(mediciones_dv)

        tiempos_fuerza_bruta.append(tiempo_fb)
        tiempos_dividir_vencer.append(tiempo_dv)

        print(
            f"n={n:5d} | "
            f"Fuerza bruta: {tiempo_fb:.6f} s | "
            f"Dividir y vencer: {tiempo_dv:.6f} s"
        )

    # Creamos la carpeta de gráficas si todavía no existe.
    carpeta_graficas = Path(__file__).parent / "graficas"
    carpeta_graficas.mkdir(parents=True, exist_ok=True)

    # Dibujamos ambas curvas en los mismos ejes.
    plt.figure(figsize=(10, 6))
    plt.plot(
        tamanos,
        tiempos_fuerza_bruta,
        marker="o",
        label="Fuerza bruta"
    )
    plt.plot(
        tamanos,
        tiempos_dividir_vencer,
        marker="s",
        label="Dividir y vencer"
    )

    plt.title("Tiempo de ejecución según el tamaño de entrada")
    plt.xlabel("Tamaño de la lista (n elementos)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    ruta_grafica = carpeta_graficas / "tiempo_vs_n.png"
    plt.savefig(ruta_grafica, dpi=150)
    plt.close()

    print(f"\nGráfica guardada en: {ruta_grafica}")


if __name__ == "__main__":
    ejecutar_mediciones()