import heapq
def algoritmo_mochila_voraz_cola_prioridad(objetos, peso_soportado):

    # Creamos una cola de prioridad en la que almacenaremos los objetos
    heap = []

    # Para cada objeto, calculamos su eficiencia y metemos los valores en la cola de prioridad con dicho valor primero, para maximizarla y que estén arriba
    for clave, (peso, valor) in objetos.items():
        eficiencia = valor / peso
        heapq.heappush(heap, (-eficiencia, clave, peso, valor))

    # Creamos una lista para almacenar los objetos seleccionados
    seleccionados = []

    # Mientras que haya valores en la cola de prioridad y el peso restante sea mayor que 0
    while heap:

        # Sacamos el primer valor (el que tenga mayor eficiencia hasta el momento) de la cola de prioridad
        eficiencia, clave, peso, valor = heapq.heappop(heap)

        # Si dicho objeto cabe, lo metemos y actualizamos la cola de prioridad
        if peso_soportado >= peso:
            seleccionados.append(clave)
            peso_soportado -= peso

    # Devolvemos la lista con los objetos seleccionados
    return seleccionados