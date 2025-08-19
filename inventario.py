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
        #copia los articulos en la pila
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

#aqui tambien se hacen las busquedas por lo que podemos usar la recursividad para encontrar el articulo