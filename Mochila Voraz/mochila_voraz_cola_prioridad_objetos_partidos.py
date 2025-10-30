import heapq


def algoritmo_mochila_voraz_cola_prioridad_objetos_partidos(objetos, peso_soportado):
    # Creamos la cola de prioridad e introducimos los valores atendiendo a la relacion valor/peso
    heap = []
    for clave, (peso, valor) in objetos.items():
        eficiencia = valor / peso
        heapq.heappush(heap, (-eficiencia, clave, peso, valor))

    # Creamos una lista de tuplas para almacenar (objeto/fraccion)
    seleccionados = []

    # Mientras que haya valores en la cola y el peso sea mayor a 0
    while heap and peso_soportado > 0:

        # Sacamos los objetos (el de mayor eficiencia en cada caso)
        eficiencia, clave, peso, valor = heapq.heappop(heap)

        # Si cabe entero, la fraccion es 1 y sino, dividimos el peso restante entre el peso del objeto para hallar su proporción
        if peso_soportado >= peso:
            fraccion = 1
            seleccionados.append((clave, fraccion))
            peso_soportado -= peso
        else:
            fraccion = peso_soportado / peso
            seleccionados.append((clave, round(fraccion, 4)))
            peso_soportado = 0

    # Devolvemos la lista de tuplas (objeto, fraccion)
    return seleccionados
