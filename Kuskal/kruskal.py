class Particion:
    """
    Clase que implementa una partición de un conjunto en subconjuntos disjuntos.
    Una partición se corresponde con una estructura Unión-Pertenencia.
    """

    def __init__(self, iterable):
        """
        Crea una partición con los elementos del iterable.
        Inicialmente cada elemento forma un subconjunto.
        """
        self.clase = {}
        self.altura = {}
        self.subconjuntos = 0
        self.tamaños = {}

        for element in iterable:
            self.clase[element] = element
            self.altura[element] = 1
            self.subconjuntos += 1
            self.tamaños[element] = 1

    def __len__(self):
        """Devuelve el número de subconjuntos en la partición."""
        return self.subconjuntos

    def numero(self, k=None):
        """
        Devuelve el número de elementos del subconjunto al que pertenece el
        elemento k.
        Si k es None devuelve el número   de elementos.
        """
        if k == None:
            return len(self.clase)
        else:
            return self.tamaños[self[k]]

    def __getitem__(self, k):
        """
        Devuelve el subconjunto al que pertenece el elemento k.
        El subconjunto se identifica mediante uno de sus elementos.
        """

        # Si el representanto de un nodo no es sí mismo, significa que hay mas nodos por encima
        if self.clase[k] != k:
            # Vamos estableciendo el representante de los nodos mientras llamamos al propio metodo hasta llegar al primero
            self.clase[k] = self.__getitem__(self.clase[k])  # Compresión de caminos
        return self.clase[k]

    def __iter__(self):
        """
        Devuelve un iterador sobre los subconjuntos.
        Cada subconjunto se identifica mediante uno de sus elementos.
        """

        vistos = set()
        for element in self.clase:
            representante = self.__getitem__(element)
            if representante not in vistos:
                vistos.add(representante)
            yield representante

    def une(self, a, b):
        """Une los subconjuntos a los que pertencen a y b."""

        # Extraemos el representante de los nodos
        rep_a = self.__getitem__(a)
        rep_b = self.__getitem__(b)

        # Si es el mismo (están en el mismo conjunto) no continuamos
        if rep_a == rep_b:
            return

        # Si el nodo a está por encima del b, entonces el representante del b será a, y el tamaño de a será el suyo mas el de b
        if self.altura[rep_a] > self.altura[rep_b]:
            self.clase[rep_b] = rep_a
            self.tamaños[rep_a] += self.tamaños[rep_b]

        # Si el nodo b está por encima de a, el representante de a será b, y el tamaño de b será el suyo mas el de a
        elif self.altura[rep_a] < self.altura[rep_b]:
            self.clase[rep_a] = rep_b
            self.tamaños[rep_b] += self.tamaños[rep_a]

        # Si ambos estuvieran a la misma altura, simplemente tomamos el primero como el más alto y ajustamos como antes
        elif self.altura[rep_a] == self.altura[rep_b]:
            self.altura[rep_a] += 1
            self.clase[rep_b] = rep_a
            self.tamaños[rep_a] += self.tamaños[rep_b]

        # Como hemos unido los dos conjuntos, ahora hay uno menos
        self.subconjuntos -= 1

def kruskal(grafo):
    """
    Dado un grafo devuelve otro grafo con el árbol expandido mínimo,
    utilizando el algoritmo de Kruskal.
    Los grafos son diccionario donde las claves son arcos (pares de nodos) y los
    valores son el peso de los arcos.
    """

    #Ordenamos los nodos por su peso
    grafo_ordenado=sorted(grafo.items(), key= lambda x: x[1])

    #Creamos un conjunto de datos para almacenar los nodos para pasarselos a la particion
    nodos=set()
    for nodo1,nodo2 in grafo.keys():
        nodos.add(nodo1)
        nodos.add(nodo2)

    particion=Particion(nodos)

    #Creamos un arbol resultado
    arbol={}

    #Para cada arista en el grafo ordenado (osea que empezamos por la primera, la de menor peso)
    for (nodo1,nodo2),peso in grafo_ordenado:

        #Si ambos nodos no pertenecen al mismo conjunto
        if particion.__getitem__(nodo1)!=particion.__getitem__(nodo2):

            #Establecemos la arista en el arbol resultado y unimos ambos nodos
            arbol[(nodo1,nodo2)]=peso
            particion.une(nodo1,nodo2)

    #Devolvemos el arbol
    return arbol