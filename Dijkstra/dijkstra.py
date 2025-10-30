def dijkstra_simple(grafo, inicial):
    """
    Implementa el algoritmo de Dijkstra
    Devuelve un diccionario con la distancia mínima desde el nodo inicial a cada uno de los nodos del grafo.
    """

    #Establecemos el nodo inicial por si no viniera definido
    if inicial is None:
        nodo=min(grafo.keys())
    else:
        nodo=inicial

    #Creamos un diccionario que se compone de una clave y una tupla, para almacenar los nodos junto con su origen y el peso del camino
    distancias={x: (None,float('inf')) for x in grafo.keys()}

    #Introducimos la distancia del nodo inicial para poder comenzar con la ejecución
    distancias[nodo]=(None,0)

    #Creamos tambien un conjunto para almacenar los nodos ya visitados
    vistos=set()


    #Hasta que el conjunto de vistos tenga la misma longitud que el grafo
    while len(vistos)<len(grafo):

        #Para cada adyacente del nodo en el que nos encontramos
        for adyacente,peso in grafo[nodo].items():

            #Si dicho adyacente no se encuentra en vistos (si se encontrara no habría que considerarlo porque ya habríamos llegado)
            if adyacente not in vistos:

                #Si el peso del adyacente es mayor que el del camino más el peso de este adyacente
                if distancias[adyacente][1]>distancias[nodo][1]+peso:

                    #Establecemos la entrada para el adyacente con el nodo del que parte y el peso calculado
                    distancias[adyacente]=(nodo,distancias[nodo][1]+peso)

        #Después, tendremos que seleccionar el nodo con menor peso entre los nodos no visitados para continuar con la siguiente iteración
        nodo=min((n for n in distancias if n not in vistos), key=lambda n: distancias[n][1])

        #Y por ultimo añadimos el nuevo nodo a la lista de vistos
        vistos.add(nodo)

    #Devolvemos el diccionario con las tuplas
    return distancias