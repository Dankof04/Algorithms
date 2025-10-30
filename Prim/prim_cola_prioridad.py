import heapq

def prim_cola_prioridad(grafo, inicial=None):


    #Establecemos el inicial, si estuviera indicado y sino, lo escogemos
    if inicial is None:
        nodo=min(grafo.keys())
    else:
        nodo=inicial

    #Creamos las estructuras de datos que constan de un conjunto de datos que almacenará los nodos ya visitados, el arbol resultado que consta de un diccionario de diccionarios y la cola de prioridad
    vistos=set()
    arbol={x:{} for x in grafo.keys()}
    heap=[]

    #Añadimos el primer nodo a la lista de vistos
    vistos.add(nodo)

    #Hasta que la lista de vistos sea igual que el grafo en cuanto a longitud
    while len(vistos)<len(grafo):

        # Para todos los adyacentes del nodo actual, los añadimos a la cola de prioridad para considerarlos después.
        for adyacente, peso in grafo[nodo].items():
            if adyacente not in vistos:
                heapq.heappush(heap, (peso, nodo, adyacente))

        #Extraemos el primer nodo de la cola de prioridad (la cola ordena los elementos atendiendo al primer campo de los mismos)
        peso, nodo, adyacente=heapq.heappop(heap)

        #Añadimos en el arbol el nodo junto a su adyacente y el peso, de forma bidireccional
        arbol[nodo][adyacente]=peso
        arbol[adyacente][nodo]=peso

        #Redefinimos el nodo para pasar al adyacente del nodo que hemos visitado y así poder ampliar sus arcos. Añadimos dicho nodo nuevo a la lista de vistos
        nodo=adyacente
        vistos.add(nodo)



    #Devolvemos el árbol
    return arbol