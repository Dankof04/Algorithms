<div id="español"></div>
<p align="right"><a href="#english">English</a></p>

## 🇪🇸 Documentación del Código

---

### Algoritmo: `algoritmo_mochila_voraz_*`

Este conjunto de funciones implementa el **problema de la mochila** (Knapsack Problem) utilizando una **estrategia voraz (greedy)**. El objetivo es seleccionar un conjunto de objetos para meter en una mochila con una capacidad de peso limitada, de tal manera que se maximice el valor total de los objetos en la mochila.

**Parámetros:**
* `objetos` (dict): Un diccionario donde cada clave es el identificador de un objeto, y su valor es una tupla `(peso, valor)`.
* `peso_soportado` (float o int): El peso máximo que la mochila puede soportar.

---

### 🏛️ Lógica y Estrategia Voraz

La estrategia voraz se basa en seleccionar siempre el objeto que ofrece la "mayor rentabilidad" primero.

1.  **Cálculo de Eficiencia:** Para cada objeto, se calcula su "eficiencia" o "rentabilidad" dividiendo su valor por su peso (`eficiencia = valor / peso`).
2.  **Selección:** El algoritmo procesa los objetos en orden descendente de eficiencia (del más rentable al menos rentable).
3.  **Iteración:** Se itera sobre los objetos y se añade cada uno a la mochila si (y cómo) cabe, actualizando el `peso_soportado` restante.

---

### 📈 Variaciones de Implementación

El núcleo del algoritmo (seleccionar por eficiencia) se implementa de dos maneras principales:

#### 1. Basada en Ordenación (`..._simple` o `..._objetos_partidos`)
* **Lógica:** Primero, se crea una lista de todos los objetos y se ordena explícitamente usando `sorted()` con una `key` basada en la eficiencia (`valor / peso`).
* **Coste:** `O(N log N)` para la ordenación, seguido de `O(N)` para la iteración. El coste dominante es `O(N log N)`.
* **Archivos:** `mochila_voraz_simple.py`, `mochila_voraz_objetos_partidos.py`.

#### 2. Basada en Cola de Prioridad (`..._cola_prioridad`)
* **Lógica:** Se utiliza un **montículo (heap)**, específicamente `heapq`, para mantener los objetos.
* **Proceso:**
    1. Se insertan todos los objetos en el montículo, usando su eficiencia *negativa* (`-eficiencia`) como clave, para simular un montículo-max (ya que `heapq` es un montículo-min).
    2. Se extrae repetidamente el objeto con la mayor eficiencia (el más negativo) del montículo (`heapq.heappop()`) y se procesa.
* **Coste:** `O(N log N)` para construir el montículo (si se insertan N elementos uno a uno) y `O(k log N)` para las `k` extracciones. El coste total sigue siendo del orden de `O(N log N)`.
* **Archivos:** `mochila_voraz_cola_prioridad.py`, `mochila_voraz_cola_prioridad_objetos_partidos.py`.

---

### 📦 Variaciones del Problema

El código aborda dos variantes fundamentales del problema de la mochila:

#### 1. Problema 0/1 (Objetos Indivisibles)
* **Descripción:** Los objetos no se pueden partir. O se toma un objeto entero, o no se toma.
* **Lógica de Selección:** Al iterar por los objetos (ya sea ordenados o extraídos del heap), si el objeto `(peso, valor)` cabe en el `peso_soportado` restante, se toma.
    * `if peso_soportado >= peso:`
    * Se añade la `clave` del objeto a la lista `seleccionados`.
    * Se reduce la capacidad: `peso_soportado -= peso`.
* **Nota:** La estrategia voraz *no garantiza* la solución óptima para el problema 0/1 (que es NP-completo). Sin embargo, es una heurística rápida y a menudo eficaz.
* **Retorna:** Una lista de claves de los objetos seleccionados.
* **Archivos:** `mochila_voraz_simple.py`, `mochila_voraz_cola_prioridad.py`.

#### 2. Problema Fraccional (Objetos Partidos)
* **Descripción:** Los objetos *sí* se pueden partir. Se puede tomar una fracción de un objeto.
* **Lógica de Selección:**
    * Si el objeto cabe entero (`peso_soportado >= peso`), se toma entero (fracción = 1).
    * Si el objeto no cabe entero pero aún queda espacio (`peso_soportado > 0`), se toma la fracción que cabe exactamente para llenar la mochila.
    * `fraccion = peso_soportado / peso`
    * La mochila se llena (`peso_soportado = 0`) y el bucle termina.
* **Nota:** La estrategia voraz *sí garantiza* la solución óptima para el problema fraccional.
* **Retorna:** Una lista de tuplas `(clave, fraccion)` para cada objeto o fracción de objeto seleccionado.
* **Archivos:** `mochila_voraz_objetos_partidos.py`, `mochila_voraz_cola_prioridad_objetos_partidos.py`.

---
<br>
<div id="english"></div>
<p align="right"><a href="#español">Español</a></p>

## 🇬🇧 Code Documentation

---

### Algorithm: `algoritmo_mochila_voraz_*`

This set of functions implements the **Knapsack Problem** using a **greedy strategy**. The goal is to select a set of items to put into a knapsack with a limited weight capacity, such that the total value of the items in the knapsack is maximized.

**Parameters:**
* `objetos` (dict): A dictionary where each key is the item's identifier, and its value is a tuple `(weight, value)`.
* `peso_soportado` (float or int): The maximum weight the knapsack can hold.

---

### 🏛️ Logic and Greedy Strategy

The greedy strategy is based on always selecting the item that offers the "best value" first.

1.  **Efficiency Calculation:** For each item, its "efficiency" or "profitability" is calculated by dividing its value by its weight (`efficiency = value / weight`).
2.  **Selection:** The algorithm processes items in descending order of efficiency (from most profitable to least profitable).
3.  **Iteration:** It iterates over the items, adding each one to the knapsack if (and how) it fits, updating the remaining `peso_soportado`.

---

### 📈 Implementation Variations

The core of the algorithm (selecting by efficiency) is implemented in two main ways:

#### 1. Sorting-Based (`..._simple` or `..._objetos_partidos`)
* **Logic:** First, a list of all items is created and explicitly sorted using `sorted()` with a `key` based on efficiency (`value / weight`).
* **Cost:** `O(N log N)` for sorting, followed by `O(N)` for iteration. The dominant cost is `O(N log N)`.
* **Files:** `mochila_voraz_simple.py`, `mochila_voraz_objetos_partidos.py`.

#### 2. Priority Queue-Based (`..._cola_prioridad`)
* **Logic:** A **heap** is used, specifically Python's `heapq`, to maintain the items.
* **Process:**
    1. All items are inserted into the heap, using their *negative* efficiency (`-efficiency`) as the key, to simulate a max-heap (since `heapq` is a min-heap).
    2. The item with the highest efficiency (most negative) is repeatedly extracted from the heap (`heapq.heappop()`) and processed.
* **Cost:** `O(N log N)` to build the heap (if inserting N items one by one) and `O(k log N)` for the `k` extractions. The total cost remains on the order of `O(N log N)`.
* **Files:** `mochila_voraz_cola_prioridad.py`, `mochila_voraz_cola_prioridad_objetos_partidos.py`.

---

### 📦 Problem Variations

The code addresses two fundamental variants of the knapsack problem:

#### 1. 0/1 Problem (Indivisible Items)
* **Description:** Items cannot be split. You either take an entire item or you don't.
* **Selection Logic:** When iterating through the items (either sorted or popped from the heap), if the item `(weight, value)` fits in the remaining `peso_soportado`, it is taken.
    * `if peso_soportado >= peso:`
    * The item's `clave` (key) is added to the `seleccionados` list.
    * The capacity is reduced: `peso_soportado -= peso`.
* **Note:** The greedy strategy *does not guarantee* the optimal solution for the 0/1 problem (which is NP-complete). However, it is a fast and often effective heuristic.
* **Returns:** A list of keys of the selected items.
* **Files:** `mochila_voraz_simple.py`, `mochila_voraz_cola_prioridad.py`.

#### 2. Fractional Problem (Divisible Items)
* **Description:** Items *can* be split. You can take a fraction of an item.
* **Selection Logic:**
    * If the item fits whole (`peso_soportado >= peso`), it is taken whole (fraction = 1).
    * If the item does not fit whole but there is still space (`peso_soportado > 0`), the fraction that fits exactly to fill the knapsack is taken.
    * `fraccion = peso_soportado / peso`
    * The knapsack becomes full (`peso_soportado = 0`) and the loop terminates.
* **Note:** The greedy strategy *does guarantee* the optimal solution for the fractional problem.
* **Returns:** A list of tuples `(clave, fraccion)` for each item or fraction of an item selected.
* **Files:** `mochila_voraz_objetos_partidos.py`, `mochila_voraz_cola_prioridad_objetos_partidos.py`.
