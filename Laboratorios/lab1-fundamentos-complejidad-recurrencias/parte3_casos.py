from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


n = 100

aleatorio = generar_aleatorio(n)
casi_ordenado = generar_casi_ordenado(n)
inverso = generar_inverso(n)

print("ESCENARIO A - ALEATORIO")
print("Primeros 20:", aleatorio[:20])
print("Ultimos 20:", aleatorio[-20:])
print()

print("ESCENARIO B - CASI ORDENADO")
print("Primeros 20:", casi_ordenado[:20])
print("Ultimos 20:", casi_ordenado[-20:])
print()

print("ESCENARIO C - INVERSO")
print("Primeros 20:", inverso[:20])
print("Ultimos 20:", inverso[-20:])

print()
print("Tamaños:")
print(len(aleatorio), len(casi_ordenado), len(inverso))

print("Elementos distintos:")
print(
    len(set(aleatorio)) == n,
    len(set(casi_ordenado)) == n,
    len(set(inverso)) == n,
)