# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Juan Felipe Torres · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `934748b`

Buen trabajo: el laboratorio funciona y está bien sustentado en sus mediciones; con los ajustes de abajo quedará aún mejor.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 14 / 20 |
| Calidad de la explicación teórica | 16 / 20 |
| Corrección de la implementación | 20 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **81 / 100** |
| **Nota (0–5)** | **4.05** |

## 1. Corrección conceptual (14 / 20)
**Lo que hizo bien:**
- Señala que dividir y vencer empieza a ganar desde n = 50 y que la ventaja es clara desde n = 100, según sus datos.
- Recomienda dividir y vencer y da una estimación a 1.000.000 de registros (unas 5,8 horas contra 2,2 segundos), declarada como estimación y razonada con las curvas teóricas, no con una regla de tres lineal.

**Lo que puede mejorar:**
- En la comparación con el máximo de un arreglo dice que dividir "añade llamadas innecesarias", pero no justifica con el costo de combinar (que es constante) ni plantea la recurrencia `T(n) = 2T(n/2) + O(1)` para mostrar que sigue siendo `Θ(n)` y no mejora.
- En el punto de cruce no explica por qué a tamaños pequeños la ventaja es mínima (las llamadas recursivas tienen un costo propio).

## 2. Calidad de la explicación teórica (16 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica de dónde salen los dos subproblemas y el trabajo lineal del caso cruzado, y la resuelve con el método maestro (caso 2, `Θ(n log n)`).
- Explica que la fuerza bruta es `Θ(n²)` porque revisa todos los pares de inicio y fin, y que acumula la suma para no recalcularla.

**Lo que puede mejorar:**
- Falta mostrar con más detalle por qué el caso cruzado cuesta `Θ(n)` (dos barridos que juntos recorren el rango) y la cuenta de cuántos pares hay en la fuerza bruta (`n(n+1)/2`).
- Conviene escribir la condición del método maestro completa: comparar `f(n)` con `n^(log₂ 2) = n` y decir que son del mismo orden.

## 3. Corrección de la implementación (20 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en las 20 listas aleatorias; no modifican la lista recibida y `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta.
- El código cumple PEP 8 y las funciones de `subarreglo.py` tienen indicaciones de tipo.

**Lo que puede mejorar:**
- Los docstrings no siguen el estilo Google: faltan las secciones `Args:` y `Returns:` (usó "Retorna:" solo en una función).
- En `medicion.py`, `medir_tiempo` y `ejecutar_mediciones` no tienen indicaciones de tipo completas y `ejecutar_mediciones` no tiene docstring.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y las dos curvas en los mismos ejes, con ocho tamaños (de 10 a 8000). Lo que dice el informe coincide con ella: en n = 8000 la fuerza bruta marca cerca de 1,34 s y dividir y vencer queda casi pegada al eje.
- Calcula los factores al duplicar n (4,54 y 4,13 para fuerza bruta; 1,95 y 2,18 para dividir y vencer) y los relaciona con el crecimiento cuadrático y `n log n`. Midió tres veces y usó la mediana.

**Lo que puede mejorar:**
- Escriba el factor que predice cada teoría (cerca de 4 para `n²` y poco más de 2 para `n log n`) y compárelo explícitamente con lo medido.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- El informe tiene su nombre, las partes en orden, la gráfica visible y enlaces a `subarreglo.py`, `pruebas.py` y `medicion.py`. Hay varios commits descriptivos sobre el laboratorio.

**Lo que puede mejorar:**
- No siguió exactamente la estructura de carpetas acordada: la carpeta se llama `Laboratorios/` (con mayúscula) en vez de `laboratorios/`.
- Las instrucciones de ejecución escriben la ruta en minúscula (`laboratorios/...`) y solo muestran comandos de Windows, así que en otros sistemas no funcionarían tal cual.
- Hay archivos `__pycache__/` publicados en el laboratorio 1; conviene agregarlos al `.gitignore`.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos coinciden en listas aleatorias y la medición corre y genera la gráfica sin errores.

## Para el próximo laboratorio
- Escriba los docstrings con las secciones `Args:` y `Returns:` y ponga indicaciones de tipo en todas las funciones, también en las de medición.
- Al comparar con la teoría, escriba el valor que esperaba y el que midió, uno junto al otro.
- Cuando compare dos formas de resolver un problema, justifique con el costo de combinar y la recurrencia.
- Revise que las rutas de las instrucciones coincidan con los nombres reales de las carpetas (mayúsculas incluidas).
