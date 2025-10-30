def algoritmo_mochila_voraz_objetos_partidos(objetos, peso_soportado):

    # Ordenamos los objetos nuevamente atendiendo a la relación valor/peso
    ordenados = sorted(objetos.items(), key=lambda x: x[1][1] / x[1][0], reverse=True)

    # Creamos una lista para los seleccionados, ahora se compondrá de una tupla (objeto,fraccion)
    seleccionados = []

    # Para cada objeto en la lista ya ordenada
    for clave, (peso, valor) in ordenados:

        # Si el peso del objeto es menor o igual, lo metemos entero (el 100%)
        if peso_soportado >= peso:
            fraccion = 1
            seleccionados.append((clave, fraccion))
            peso_soportado -= peso

        # Si el peso del objeto es mayor al soportado, dividimos el peso soportado entre el peso para ver que cantidad del peso del objeto supone
        else:
            fraccion = peso_soportado / peso
            seleccionados.append((clave, round(fraccion, 4)))

            # Establecemos el peso restante a 0, porque si quedara peso restante habríamos metido el objeto entero
            peso_soportado = 0

    # Devolvemos la lista de tuplas
    return seleccionados