# Retroalimentación — Laboratorio 3: Estructuras de datos

**Estudiante:** Juan Felipe Torres Torres · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `aea0f6c`

Muy buen trabajo en la implementación y en las gráficas.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 17 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **93 / 100** |
| **Nota (0–5)** | **4.65** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien la colisión con el ejemplo de las guías 10, 24 y 17 con m = 7, y compara encadenamiento con direccionamiento abierto.
- Justifica que la tabla hash no sirve para rangos porque no conserva el orden.
- Estima la altura del árbol degenerado (unas 400.000) y la del equilibrado (cerca de 19), y recomienda tabla hash más árbol equilibrado.
- Declara la estimación a 5.000.000 como estimación y justifica que la lista crece de forma lineal.

**Lo que puede mejorar (y cómo corregirlo):**
- La estimación para la tabla hash solo repite el tiempo medido, sin explicar por qué debería mantenerse así con 5.000.000 de envíos.
  → *Cómo corregirlo:* piense qué le pasa a α si m crece junto con n y qué otros factores (como la memoria) podrían cambiar el tiempo real, y escríbalo en un par de frases.
- La comparación del árbol equilibrado con el degenerado no dice cuántas veces más rápido sería la búsqueda.
  → *Cómo corregirlo:* compare con una división o una frase los dos números de comparaciones que ya calculó.

## 2. Calidad de la explicación teórica (17 / 20)
**Lo que hizo bien:**
- Nombra correctamente Θ(n) para la lista y Θ(1 + α) para la tabla, el supuesto de hash uniforme simple y que, si todas las guías caen en una casilla, se degrada a Θ(n).

**Lo que puede mejorar (y cómo corregirlo):**
- No explica por qué la lista recorre todos los nodos en el caso infructuoso.
  → *Cómo corregirlo:* describa en una frase qué condición permite al recorrido detenerse y por qué una guía inexistente nunca la cumple.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Lista y tabla devuelven el estado correcto en búsquedas exitosas e infructuosas; la colisión forzada con m = 7 funciona y `factor_carga` da 3/7.
- La tabla reutiliza la lista y no usa `dict`, `set` ni `hash()`; `buscar` es iterativo.
- Las pruebas cubren veinte colecciones aleatorias con guías existentes e inexistentes.
- Todas las funciones tienen docstrings con `Args` y `Returns`, type hints y dos líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen y están bien hechas: título, ejes rotulados, leyenda, seis valores de n y cuatro valores de α.
- En la pregunta 2 calcula factores de crecimiento de la lista (5,65; 4; 2,82) y los contrasta con Θ(n); los datos coinciden con lo que se lee en la gráfica.

**Lo que puede mejorar (y cómo corregirlo):**
- Para la tabla hash no calcula factores de crecimiento entre dos valores de n; solo dice que los tiempos "permanecieron entre" dos cifras.
  → *Cómo corregirlo:* divida el tiempo de la tabla en dos valores consecutivos de n y compárelo con cuánto creció n.
- Dice que el aumento con α es "concordante" con Θ(1 + α) sin ningún cálculo.
  → *Cómo corregirlo:* tome dos valores de α, calcule cuántas veces creció el tiempo y compárelo con cuántas veces creció 1 + α.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- El informe sigue el orden pedido, las imágenes se ven con rutas relativas, cada parte enlaza su código y hay tres commits con mensajes descriptivos.

**Lo que puede mejorar (y cómo corregirlo):**
- No siguió exactamente la estructura de carpetas acordada: usó `Laboratorios/` con mayúscula inicial. Queda anotado como incumplimiento de convención, sin descuento de puntos.
  → *Cómo corregirlo:* renombre con `git mv Laboratorios laboratorios` (en dos pasos si su sistema no distingue mayúsculas).
- Las instrucciones de reproducción usan la ruta `laboratorios/lab3-estructuras-datos/...` en minúscula, que no coincide con el nombre real de la carpeta, y el comando de activación solo sirve en Windows.
  → *Cómo corregirlo:* escriba la ruta tal como existe en el repositorio y agregue el comando equivalente para macOS y Linux.

## ¿El código funciona?
Sí. Las pruebas pasan, las dos estructuras dan el mismo resultado y las mediciones se ejecutan y regeneran las dos gráficas sin errores.
