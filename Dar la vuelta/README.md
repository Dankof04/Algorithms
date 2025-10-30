<div id="español"></div>
<p align="right"><a href="#english">English</a></p>

## 🇪🇸 Documentación del Código

---

### Función: `dar_la_vuelta(cambio, valores_monedas)`

Esta función implementa un generador que calcula la combinación óptima de monedas para devolver una cantidad de cambio específica, minimizando el número total de monedas utilizadas. Utiliza un enfoque "voraz" (greedy), seleccionando siempre la moneda de mayor valor posible en cada paso.

**Parámetros:**
* `cambio` (float): La cantidad total de dinero que se debe devolver.
* `valores_monedas` (list): Una lista o tupla de números (int o float) que representan los valores de las monedas disponibles (ej. `[0.01, 0.05, 0.1, 0.5, 1, 2]`).

**Retorna:**
* (Generator): Un generador que produce (devuelve con `yield`) el valor de cada moneda necesaria para componer el cambio, una por una, de mayor a menor valor.

---

### 🏛️ Lógica Interna Detallada

El algoritmo sigue los siguientes pasos:

1.  **Ordenar Monedas:**
    ```python
    valores_monedas = sorted(valores_monedas, reverse=True)
    ```
    Primero, se ordena la lista `valores_monedas` en orden **descendente** (de mayor a menor). Esto es crucial para el algoritmo voraz, ya que garantiza que siempre intentaremos usar la moneda de mayor valor disponible primero.

2.  **Redondear Cambio Inicial:**
    ```python
    cambio = round(cambio, 2)
    ```
    Se redondea la cantidad de cambio inicial a dos decimales. Esto es una medida de seguridad esencial en Python para evitar problemas de precisión con números de punto flotante (floats) al realizar operaciones aritméticas, algo común al trabajar con dinero.

3.  **Bucle Principal (Mientras quede cambio):**
    ```python
    while cambio > 0:
    ```
    Se inicia un bucle `while` que continuará ejecutándose mientras la cantidad de cambio pendiente (`cambio`) sea mayor que cero.

4.  **Iterar sobre Monedas:**
    ```python
    for element in valores_monedas:
    ```
    Dentro del bucle `while`, se itera sobre la lista de monedas (ya ordenada de mayor a menor).

5.  **Comprobar si la Moneda "Cabe":**
    ```python
    if cambio >= element:
    ```
    Se comprueba si el cambio restante es mayor o igual al valor de la moneda actual (`element`).

6.  **Devolver la Moneda (Yield):**
    ```python
    yield element
    ```
    Si la moneda "cabe", se "devuelve" (produce) esa moneda usando `yield`. Esto pausa la ejecución de la función y entrega el valor `element` al código que esté iterando sobre el generador.

7.  **Actualizar el Cambio Restante:**
    ```python
    cambio = round(cambio - element, 2)
    ```
    Se resta el valor de la moneda (`element`) del cambio restante. Nuevamente, se utiliza `round()` para mantener la precisión de dos decimales y evitar errores de flotantes.

8.  **Reiniciar el Bucle Interno:**
    ```python
    break
    ```
    Tras encontrar una moneda válida y restarla, se utiliza `break` para salir del bucle `for` interno. Esto fuerza al bucle `while` a iniciar una nueva iteración, comenzando de nuevo la comprobación desde la moneda de mayor valor. Esto es fundamental para casos donde se necesita usar la misma moneda varias veces (ej. devolver 0.40 usando dos monedas de 0.20).

---
<br>
<div id="english"></div>
<p align="right"><a href="#español">Español</a></p>

## 🇬🇧 Code Documentation

---

### Function: `dar_la_vuelta(cambio, valores_monedas)`

This function implements a generator that calculates the optimal combination of coins to return a specific amount of change, minimizing the total number of coins used. It employs a "greedy" approach, always selecting the highest value coin possible at each step.

**Parameters:**
* `cambio` (float): The total amount of money to be returned.
* `valores_monedas` (list): A list or tuple of numbers (int or float) representing the available coin denominations (e.g., `[0.01, 0.05, 0.1, 0.5, 1, 2]`).

**Returns:**
* (Generator): A generator that yields the value of each coin needed to make the change, one by one, from largest to smallest value.

---

### 🏛️ Detailed Internal Logic

The algorithm follows these steps:

1.  **Sort Coins:**
    ```python
    valores_monedas = sorted(valores_monedas, reverse=True)
    ```
    First, the `valores_monedas` list is sorted in **descending** order (from largest to smallest). This is crucial for the greedy algorithm, ensuring we always try to use the largest available coin value first.

2.  **Round Initial Change:**
    ```python
    cambio = round(cambio, 2)
    ```
    The initial change amount is rounded to two decimal places. This is an essential safeguard in Python to prevent precision issues with floating-point numbers (floats) when performing arithmetic, a common problem when working with currency.

3.  **Main Loop (While change remains):**
    ```python
    while cambio > 0:
    ```
    A `while` loop is initiated, which will continue to run as long as the pending change amount (`cambio`) is greater than zero.

4.  **Iterate Over Coins:**
    ```python
    for element in valores_monedas:
    ```
    Inside the `while` loop, it iterates over the list of coins (already sorted from largest to smallest).

5.  **Check if the Coin "Fits":**
    ```python
    if cambio >= element:
    ```
    It checks if the remaining change is greater than or equal to the value of the current coin (`element`).

6.  **Return the Coin (Yield):**
    ```python
    yield element
    ```
    If the coin "fits," it is "returned" (produced) using `yield`. This pauses the function's execution and delivers the `element` value to the code that is iterating over the generator.

7.  **Update Remaining Change:**
    ```python
    cambio = round(cambio - element, 2)
    ```
    The value of the coin (`element`) is subtracted from the remaining change. Again, `round()` is used to maintain two-decimal precision and avoid floating-point errors.

8.  **Restart the Inner Loop:**
    ```python
    break
    ```
    After finding a valid coin and subtracting it, `break` is used to exit the inner `for` loop. This forces the `while` loop to start a new iteration, beginning the check again from the largest coin value. This is fundamental for cases where the same coin needs to be used multiple times (e.g., returning 0.40 using two 0.20 coins).
