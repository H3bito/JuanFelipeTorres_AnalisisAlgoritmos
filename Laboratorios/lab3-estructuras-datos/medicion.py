"""Experimentos de rendimiento para la lista enlazada y la tabla hash."""

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


DIRECTORIO = Path(__file__).resolve().parent
DIRECTORIO_GRAFICAS = DIRECTORIO / "graficas"
REPETICIONES = 200
TAMANO_FIJO = 20_000


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: Guias almacenadas en las estructuras.
        cantidad: Cantidad de guias inexistentes que se generaran.
        semilla: Semilla para reproducir la medicion.

    Returns:
        Una lista de guias que no pertenecen a existentes.
    """
    azar = random.Random(semilla)
    inexistentes = []

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)

    return inexistentes


def es_primo(numero: int) -> bool:
    """Determina si un numero entero es primo.

    Args:
        numero: Numero que se desea evaluar.

    Returns:
        True si el numero es primo, False en caso contrario.
    """
    if numero < 2:
        return False

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


def siguiente_primo(numero: int) -> int:
    """Encuentra el primer primo mayor o igual que un numero.

    Args:
        numero: Limite inferior de la busqueda.

    Returns:
        El primer numero primo encontrado.
    """
    candidato = max(2, numero)

    while not es_primo(candidato):
        candidato += 1

    return candidato


def construir_datos(
    cantidad: int, semilla: int
) -> tuple[list[tuple[int, str]], set[int]]:
    """Genera guias unicas y sus estados.

    Args:
        cantidad: Numero de guias que se generaran.
        semilla: Semilla para reproducir los datos.

    Returns:
        Los pares guia-estado y el conjunto de guias existentes.
    """
    azar = random.Random(semilla)
    guias = azar.sample(range(10**9, 10**10), cantidad)
    estados_posibles = ["en bodega", "en reparto", "entregado"]

    datos = [
        (guia, azar.choice(estados_posibles))
        for guia in guias
    ]

    return datos, set(guias)


def construir_estructuras(
    datos: list[tuple[int, str]], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye la lista y la tabla con los mismos datos.

    Args:
        datos: Pares de guia y estado.
        m: Numero de casillas de la tabla hash.

    Returns:
        La lista enlazada y la tabla hash construidas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)

    for guia, estado in datos:
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    return lista, tabla


def verificar_estructuras(
    lista: ListaEnlazada,
    tabla: TablaHash,
    datos: list[tuple[int, str]],
) -> None:
    """Comprueba que ambas estructuras devuelvan los mismos estados.

    Args:
        lista: Lista enlazada construida.
        tabla: Tabla hash construida.
        datos: Pares de guia y estado que se almacenaron.
    """
    muestra = datos[:min(100, len(datos))]

    for guia, estado in muestra:
        assert lista.buscar(guia) == estado
        assert tabla.buscar(guia) == estado


def medir_busquedas(
    estructura: ListaEnlazada | TablaHash,
    consultas: list[int],
) -> float:
    """Calcula el tiempo medio de una busqueda infructuosa.

    Args:
        estructura: Estructura en la que se buscara.
        consultas: Guias que no existen en la estructura.

    Returns:
        Tiempo medio por busqueda, en segundos.
    """
    # Verificar los resultados antes de iniciar el cronometro.
    for guia in consultas:
        assert estructura.buscar(guia) is None

    # Cronometrar solamente las llamadas de busqueda.
    inicio = time.perf_counter()

    for guia in consultas:
        estructura.buscar(guia)

    fin = time.perf_counter()
    return (fin - inicio) / len(consultas)


def experimento_a() -> None:
    """Compara las busquedas en lista enlazada y tabla hash."""
    tamanos = [100, 500, 1_000, 5_000, 20_000, 50_000]
    tiempos_lista = []
    tiempos_tabla = []

    print("\nEXPERIMENTO A: LISTA FRENTE A TABLA HASH")
    print("n\tm\tLista (s)\tTabla (s)")

    for n in tamanos:
        datos, existentes = construir_datos(n, semilla=100 + n)

        # La tabla usa un primo cercano a n / 2.
        m = siguiente_primo(max(2, n // 2))

        lista, tabla = construir_estructuras(datos, m)
        verificar_estructuras(lista, tabla, datos)

        consultas = generar_guias_inexistentes(
            existentes, REPETICIONES, semilla=7 + n
        )

        tiempo_lista = medir_busquedas(lista, consultas)
        tiempo_tabla = medir_busquedas(tabla, consultas)

        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)

        print(
            f"{n}\t{m}\t{tiempo_lista:.8f}\t"
            f"{tiempo_tabla:.8f}"
        )

    DIRECTORIO_GRAFICAS.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 6))
    plt.plot(
        tamanos, tiempos_lista, marker="o",
        label="Lista enlazada"
    )
    plt.plot(
        tamanos, tiempos_tabla, marker="s",
        label="Tabla hash"
    )
    plt.title("Tiempo medio de busqueda frente al numero de guias")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(DIRECTORIO_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close()


def experimento_b() -> None:
    """Mide el efecto del factor de carga en la tabla hash."""
    n = TAMANO_FIJO
    datos, existentes = construir_datos(n, semilla=2026)
    consultas = generar_guias_inexistentes(
        existentes, REPETICIONES, semilla=77
    )

    # Los tamanos producen factores de carga 0.5, 1, 4 y 10.
    factores_objetivo = [0.5, 1.0, 4.0, 10.0]
    factores_reales = []
    tiempos = []

    print("\nEXPERIMENTO B: EFECTO DEL FACTOR DE CARGA")
    print("n\tm\tAlfa\tTiempo medio (s)")

    for alfa_objetivo in factores_objetivo:
        m = round(n / alfa_objetivo)
        tabla = TablaHash(m)

        for guia, estado in datos:
            tabla.insertar(guia, estado)

        # Comprobar que las busquedas existentes sean correctas.
        for guia, estado in datos[:100]:
            assert tabla.buscar(guia) == estado

        alfa = tabla.factor_carga()
        tiempo = medir_busquedas(tabla, consultas)

        factores_reales.append(alfa)
        tiempos.append(tiempo)

        print(f"{n}\t{m}\t{alfa:.2f}\t{tiempo:.8f}")

    DIRECTORIO_GRAFICAS.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 6))
    plt.plot(factores_reales, tiempos, marker="o", label="Tabla hash")
    plt.title("Tiempo medio de busqueda frente al factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(DIRECTORIO_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close()


def main() -> None:
    """Ejecuta los dos experimentos y genera las graficas."""
    experimento_a()
    experimento_b()
    print("\nMediciones terminadas. Graficas guardadas correctamente.")


if __name__ == "__main__":
    main()
