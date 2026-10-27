"""Pruebas de la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_busquedas_basicas() -> None:
    """Verifica busquedas exitosas e infructuosas."""
    lista = ListaEnlazada()
    tabla = TablaHash(7)

    datos = [
        (1000000010, "en bodega"),
        (1000000024, "en reparto"),
        (1000000017, "en bodega"),
        (1000000005, "entregado"),
    ]

    for guia, estado in datos:
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    for guia, estado in datos:
        assert lista.buscar(guia) == estado
        assert tabla.buscar(guia) == estado

    assert lista.buscar(9999999999) is None
    assert tabla.buscar(9999999999) is None


def probar_colisiones() -> None:
    """Verifica el encadenamiento de tres guias en una casilla."""
    tabla = TablaHash(7)
    guias = (10, 24, 17)

    for guia in guias:
        assert tabla.hash(guia) == 3
        tabla.insertar(guia, "en bodega")

    for guia in guias:
        assert tabla.buscar(guia) == "en bodega"

    assert tabla.casillas[3].tamano == 3
    assert tabla.factor_carga() == 3 / 7
    assert tabla.buscar(31) is None


def probar_colecciones_aleatorias() -> None:
    """Compara ambas estructuras en veinte colecciones aleatorias."""
    azar = random.Random(42)

    for _ in range(20):
        cantidad = azar.randint(1, 100)
        guias = azar.sample(range(10**9, 10**10), cantidad)
        tabla = TablaHash(azar.choice([7, 11, 17, 31, 53]))
        lista = ListaEnlazada()
        estados = {}

        for guia in guias:
            estado = azar.choice(
                ["en bodega", "en reparto", "entregado"]
            )
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)
            estados[guia] = estado

        # Todas las guias existentes deben devolver el mismo estado.
        for guia, estado in estados.items():
            assert lista.buscar(guia) == estado
            assert tabla.buscar(guia) == estado
            assert lista.buscar(guia) == tabla.buscar(guia)

        # Las guias inexistentes deben devolver None en ambas.
        inexistentes = azar.sample(
            range(10**9, 10**10),
            20,
        )

        for guia in inexistentes:
            if guia not in estados:
                assert lista.buscar(guia) is None
                assert tabla.buscar(guia) is None
                assert lista.buscar(guia) == tabla.buscar(guia)


def main() -> None:
    """Ejecuta todas las pruebas del laboratorio."""
    probar_busquedas_basicas()
    probar_colisiones()
    probar_colecciones_aleatorias()
    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    main()
