# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Juan Felipe Torres · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `eff6303`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 14 / 25 |
| Calidad de la explicación teórica | 15 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 13 / 20 |
| Documentación y organización del informe | 5 / 10 |
| **Total** | **62 / 100** |
| **Nota (0–5)** | **3.10** |

## 1. Corrección conceptual (14 / 25)
**Lo que hizo bien:**
- Distingue entre que el algoritmo sea correcto y que sea rápido, y nombra la ventana de cuatro horas como la restricción que no se cumple.
- Explica que duplicar la velocidad del servidor solo mejora por un factor constante y el problema de fondo (crecimiento cuadrático) sigue ahí.
- Menciona que el orden de la lista decide a quién se contacta primero.

**Lo que puede mejorar:**
- El segundo ejemplo (búsqueda secuencial vs. binaria) es muy general: no dice qué sistema es, cuántos datos tiene ni qué restricción se incumple.
- En la Parte 2 falta explicar cómo el tiempo de ejecución se vuelve energía gastada y cómo se acumula todas las madrugadas durante años.
- Los perjuicios a personas son vagos ("la organización, quienes trabajan allí"). Faltan al menos dos casos concretos de una persona afectada y decir con claridad quién asume el costo en cada uno (paciente, operador, Secretaría, equipo de desarrollo).
- Falta la obligación adicional que impone el orden de la lista: que el ordenamiento sea correcto, no solo rápido.

## 2. Calidad de la explicación teórica (15 / 25)
**Lo que hizo bien:**
- Plantea la recurrencia de merge sort, aplica el método maestro identificando `a`, `b` y `f(n)`, verifica la condición del caso 2 y llega a `Θ(n log n)`.
- Deja la predicción escrita antes del experimento y presenta la tabla de complejidades.
- El cálculo de comparaciones de insertion sort en mejor y peor caso (`n - 1` y `n(n-1)/2`) es correcto.

**Lo que puede mejorar:**
- No explica de dónde sale cada término de `T(n) = 2T(n/2) + Θ(n)` (por qué dos subproblemas, por qué la mitad, por qué `n` al mezclar).
- Los tres casos no se definen indicando sobre qué conjunto de entradas se toma el máximo, el mínimo o el promedio.
- No dice cuál de los tres casos usaría para decidir si el algoritmo entra en producción ni por qué.
- El análisis de insertion sort no va línea por línea: no indica cuántas veces se ejecuta cada línea ni suma los costos.
- La predicción dice que "se comprobó", pero no la contrasta con detalle con lo medido.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor), no cambian la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`. El conteo da `n - 1` en el mejor caso.
- Los tres generadores dan listas del tamaño pedido, sin repetidos, y los aleatorios usan semilla.
- `merge_sort` tiene su propia mezcla recursiva.

**Lo que puede mejorar:**
- La función interna `dividir_y_ordenar` no tiene docstring.
- Varias funciones de `parte3_casos.py` y `parte4_complejidad.py` no indican el tipo de lo que devuelven o reciben (`generador`, `algoritmo`, `resultados`), y `medir_algoritmo` no documenta sus parámetros.
- Faltan dos líneas en blanco entre funciones en `algoritmos.py` y `datos.py`.

## 4. Calidad del análisis de las gráficas (13 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados, leyenda y las curvas en los mismos ejes.
- Identifica correctamente el inverso como peor caso, el casi ordenado como mejor y el aleatorio como intermedio, con datos medidos.
- Concluye con datos propios (n = 6400: 0,759 s contra 0,011 s) que merge sort es mejor y que coincide con la teoría.
- Aclara que la extrapolación a 1.200.000 registros es teórica y no una medición.

**Lo que puede mejorar:**
- La extrapolación a la ventana de cuatro horas no se calcula: no dice si cada algoritmo cabe o no en esas cuatro horas.
- La respuesta a la compra del servidor no se apoya en un número medido (por ejemplo, cuánto tendría que mejorar el hardware frente a la diferencia de 69 veces).
- El único aspecto adicional al tiempo es la energía; faltan memoria extra de merge sort, estabilidad o mantenimiento.
- No explica cómo recomendar un solo algoritmo si el canal de entrada puede cambiar sin aviso.

## 5. Documentación y organización del informe (5 / 10)
**Lo que hizo bien:**
- Enlaza `algoritmos.py`, `datos.py`, `parte3_casos.py` y `parte4_complejidad.py` desde el informe, y las tres gráficas se ven incrustadas.
- Hay más de cinco commits descriptivos del laboratorio.

**Lo que puede mejorar:**
- No siguió la estructura de carpetas acordada: el laboratorio está en `Laboratorios/` con L mayúscula, y la ubicación acordada es `laboratorios/` en minúscula (en GitHub son carpetas distintas).
- Subió archivos `__pycache__/*.pyc` dentro de la carpeta del laboratorio; esos archivos no deben publicarse.
- La entrega está en la rama `master` y no en `main`.
- El informe no trae su nombre completo ni las instrucciones para reproducir el experimento (activar el entorno y comando de cada parte).
- La sección del concepto técnico quedó numerada como 4.4, y la parte de merge sort y el análisis línea por línea están en un orden distinto al pedido.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien en todas mis pruebas, y los dos scripts corren sin errores y generan las gráficas. Los resultados que obtuve son parecidos a los de su informe.

## Para el próximo laboratorio
- Use la carpeta `laboratorios/` en minúscula, trabaje en la rama `main` y agregue `__pycache__/` al archivo `.gitignore`.
- Ponga su nombre y los comandos para reproducir el experimento al inicio del informe.
- Dé ejemplos concretos (qué sistema, cuántos datos, qué límite se incumple) y nombre a las personas afectadas y quién asume el costo.
- Desarrolle el análisis línea por línea y explique de dónde sale cada parte de la recurrencia.
- Calcule la extrapolación con números a partir de sus mediciones y use ese dato para responder a la compra del servidor.
