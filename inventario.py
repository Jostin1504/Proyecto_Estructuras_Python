#La lista va a manejar pilas de articulos iguales
class PilaArticulos:
    def __init__(self):
        self.items = []

    def apilar(self, items):
       self.items.append(items)

    def desapilar(self):
        #si no hay items
        if not self.items:
            return None
        #si, si hay
        return self.items.pop()
    
    def __str__(self):
        return f" Articulos apilados: {len(self.items)}"
#como todos los objetos de los articulos son iguales no hace falta moverlos

class Nodo:
    def __init__(self, articulo):
        self.dato = articulo
        self.pila = PilaArticulos()  # Cada nodo tiene su propia pila de artículos
                                     #copia los articulos en la pila por la cantidad ingresada
        for _ in range(articulo.cantidad):
            self.pila.apilar(articulo)

        self.siguiente = None #ve la pila siguiente
        self.anterior = None  #ve la pila anterior
        
#lista doblemente enlazada para mas practicidad
class ListaInventario:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_articulo(self, articulo):
        nuevo_nodo = Nodo(articulo)
        if not self.primero:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo

    #Clase basica para mostrar que es doble:
    def mostrar_articulos(self):
        actual = self.primero
        while actual:
            print(actual.dato)        
            print(actual.pila)        
            print(" -----------\n")
            actual = actual.siguiente

    #para que sirve este metodo?
    #debido a que se manejan pilas de articulos copia, este metodo permite obtener una lista de nodos
    #en otras palabras agarrar toda la pila
    @staticmethod
    def pasar_a_lista_nodos(lista_inventario):
        nodos = []
        actual = lista_inventario.primero
        while actual:
            nodos.append(actual)
            actual = actual.siguiente
        return nodos
    
    #metodos de ordenamiento selecction sort
    @staticmethod  #metodo para llamar sin instancia lo que seria un STATIC en c++
    def ordenarPorCantidad(lista_nodos):
        ordenada = []
        copia = lista_nodos[:] #copia la lista original
        while copia:
            menor = copia[0]
            for item in copia:
                if len(item.pila.items) < len(menor.pila.items): # Compara la can de articulos
                    menor = item
            ordenada.append(menor)
            copia.remove(menor)

    def ordenXcan(self):
        # Obtiene los nodos en una lista
        nodos = self.pasar_a_lista_nodos(self)
        # Ordena los nodos por cantidad
        ordenados = self.ordenarPorCantidad(nodos)
        # Reconstruye la lista enlazada
        self.primero = None
        self.ultimo = None
        for nodo in ordenados:
            nodo.anterior = None
            nodo.siguiente = None
            if not self.primero:
                self.primero = nodo
                self.ultimo = nodo
            else:
                self.ultimo.siguiente = nodo
                nodo.anterior = self.ultimo
                self.ultimo = nodo

    @staticmethod
    def ordenarPorPrecios(lista_nodos):
        ordenada = []
        copia = lista_nodos[:]
        while copia:
            menor = copia[0]
            for item in copia:
                if len(item.pila.items.precio) < len(menor.pila.items.precio):
                    menor = item
            ordenada.append(menor)
            copia.remove(menor)
        return ordenada

    @staticmethod
    def ordenarAlfabeticamente(lista_nodos):
        ordenada = []
        copia = lista_nodos[:]
        while copia:
            menor = copia[0]
            for item in copia:
                if len(item.nombre.lower()) < menor.nombre.lower():
                    menor = item
            ordenada.append(menor)
            copia.remove(menor)
        return ordenada

    #metodo de busqueda
    def buscar_articulo_nombre(self, nombre):
        actual = self.primero
        while actual:
            if actual.dato.nombre.lower() == nombre.lower():
                return actual.dato
            actual = actual.siguiente
        return None
    
    def buscar_articulo_tipo(self, tipo):
        actual = self.primero
        while actual:
            if actual.dato.tipo.lower() == tipo.lower():
                return actual.dato
            actual = actual.siguiente
        return None
    
    #este metodo esta hecho para que solo elimine despues de completar con exito la compra
    def eliminar_articulo(self, nombre, cantidad):
        actual = self.primero
        while actual:
            if actual.dato.nombre.lower() == nombre.lower():
                for _ in range(cantidad):
                    actual.pila.desapilar()
                if not actual.pila.items:
                    # Si la oila esta vacia se vuela el nodo
                    if actual.anterior:
                        actual.anterior.siguiente = actual.siguiente

                    else:
                        self.primero = actual.siguiente
                    if actual.siguiente:
                        actual.siguiente.anterior = actual.anterior
                    else:
                        self.ultimo = actual.anterior
                return True
            actual = actual.siguiente
        return False

    #Este metodo comprueba la cantidad de la pila para evitar que el usuario 
    #intente comprar mas de los que hay 
    def verificar_cantidad_articulo(self, nombre, cantidad):
        actual = self.primero
        while actual:
            if actual.dato.nombre.lower() == nombre.lower():
                return len(actual.pila.items) >= cantidad
            actual = actual.siguiente
        return False 
        