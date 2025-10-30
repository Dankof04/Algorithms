import heapq

def dijkstra_cola_prioridad(grafo, inicial):

    #Establecemos el nodo inicial si no viniera dado
    if inicial is None:
        nodo=min(grafo.keys())
    else:
        nodo=inicial

    #Creamos el conjunto para almacenar los nodos vistos
    vistos=set()

    #Creamos el diccionario compuesto por claves y tuplas en el que almacenamos los nodos con su origen y su peso
    distancias={x:(None,float('inf')) for x in grafo.keys()}

    #Introducimos el primer nodo
    distancias[nodo]=(None,0)

    #Creamos la cola de prioridad e introducimos el valor del primer nodo en la misma
    heap=[]
    heapq.heappush(heap,(0,nodo))

    #Mientras que la cola de prioridad tenga algo y la longitud de vistos sea menor que el grafo
    while heap and len(vistos)<len(grafo):

        #Extraemos el nodo con menor peso dentro de la cola de prioridad
        peso,nodo=heapq.heappop(heap)

        #Lo añadimos a vistos y desarrollamos sus adyacentes
        vistos.add(nodo)
        for adyacente,peso_nuevo in grafo[nodo].items():
            if adyacente not in vistos:

                #Si el adyacente no está en vistos y la distancia del adyacente es mayor que la del nodo más el peso nuevo
                if distancias[adyacente][1]>distancias[nodo][1]+peso_nuevo:

                    #Introducimos el valor en la cola de prioridad y sobreescribimos el peso en distancias, actualizandolo al menor
                    heapq.heappush(heap,(distancias[nodo][1]+peso_nuevo,adyacente))
                    distancias[adyacente]=(nodo,distancias[nodo][1]+peso_nuevo)

    #Devolvemos el diccionario
    return distancias