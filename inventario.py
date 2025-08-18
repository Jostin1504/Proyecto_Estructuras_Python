class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

#en primera instancia usariamos la lista para los inventarios de articulos
#lista doblemente enlazada para mas practicidad
class ListaInventario:
    def __init__(self):
        self.primero = None

    def agregar_articulo(self, articulo):
        nuevo_nodo = Nodo(articulo)
        if not self.primero:
            self.primero = nuevo_nodo
        else:
            actual = self. primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def mostrar_articulos(self):
        actual = self.primero
        while actual:
            print(f"articulo: {actual.dato}")
            actual = actual.siguiente
    #Clase basica para mostrar que es doble:
    def mostrar_articulos_reversa(self):
        actual = self.primero
        if not actual:
            print("No hay articulos en el inventario.")
            return
        while actual.siguiente:
            actual = actual.siguiente
        while actual:
            print(f"articulo: {actual.dato}")
            actual = actual.anterior

#aqui tambien se hacen las busquedas por lo que podemos usar la recursividad para encotrar el articulo