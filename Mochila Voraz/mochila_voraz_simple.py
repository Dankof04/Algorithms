def algoritmo_mochila_voraz_simple(objetos, peso_soportado):
    """
    Se recibe un diccionario de objetos, cada elemento del diccionario es una tupla (peso, valor)
    y una variable numérica, peso_soportado.
    Seleccionar las claves de los objetos cuya suma del peso no sea mayor que el peso soportado y se
    maximice el valor usando un algoritmo voraz. Los objetos no pueden partirse.
    """

    #Ordenamos los objetos según su relación valor/peso (los objetos vienen dados por una clave y una tupla), así que el peso está en la coordenada [1][0] y el valor en la [1][1]
    ordenados=sorted(objetos.items(), key=lambda x: x[1][1] / x[1][0],reverse=True)

    #Creamos una lista para los valores seleccionados
    seleccionados=[]

    #Para cada objeto en la lista ya ordenada
    for clave, (peso,valor) in ordenados:

        #Si el peso del objeto es menor o igual al peso soportado, lo metemos
        if peso_soportado>=peso:

            #Metemos la clave en la lista de seleccionados y actualizamos el peso soportado restante
            seleccionados.append(clave)
            peso_soportado-=peso

    #Devolvemo la lista de objetos seleccionados
    return seleccionados
