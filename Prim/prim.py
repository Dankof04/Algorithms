def prim(grafo, inicial=None):
    """
    Implementa el algoritmo de Prim para obtener el árbol de expansión mínima de un grafo. Devuelve en el formato del grafo el árbol.

    Se recuerda que un árbol es un grafo sin bucles y conectado.

    El grafo que se va a recibir siempre será conexo y sin direcciones.
    """

    #Establecemos el inicial, lo renombro para que sea mas intuitivo. Si no está definido cogemos el menor de las claves (la A)
    if inicial is None:
        nodo=min(grafo.keys())
    else: nodo=inicial

    #Creamos las estructuras de datos necesarias: un conjunto para almacenar los vistos, el arbol resultado que es un diccionario de diccionarios y un diccionario de tuplas en el que almacenamos un nodo, su origen y el coste del camino
    vistos=set()
    arbol={x: {} for x in grafo.keys()}
    candidatos={x: (None, float('inf')) for x in grafo.keys()}

    #Añadimos el primer nodo a la lista de vistos
    vistos.add(nodo)

    #Hasta que no se hayan visitado todos los nodos
    while len(vistos) < len(grafo):

        #Para cada adyacente del nodo del que partimos
        for adyacente,peso in grafo[nodo].items():
            #Si el nodo no está en vistos (si estuviera significaría que lo hemos visitado)
            if adyacente not in vistos:
                #Si el peso del adyacente es menor que el peso establecido en "candidatos" (partiendo de infinito)
                if peso<candidatos[adyacente][1]:
                    #Actualizamos el peso y metemos el candidato si no estuviera
                    candidatos[adyacente]=(nodo,peso)

        #Escogemos el candidato con menor peso, tratandose de [nodo, (origen,peso)], el peso estaría en [1][1]
        mejor=min(candidatos.items(), key=lambda x: x[1][1])

        #Asignamos a cada nodo su origen y peso (como no es dirigido tenemos que hacerlo en ambas direcciones
        arbol[mejor[0]][mejor[1][0]]=mejor[1][1]
        arbol[mejor[1][0]][mejor[0]]=mejor[1][1]

        #Sacamos el nodo de candidatos para no volverlo a elegir y actualizamos nodo, añadiendolo en vistos
        candidatos.pop(mejor[0])
        nodo=mejor[0]
        vistos.add(nodo)

    #Devolvemos el arbol conformado
    return arbol