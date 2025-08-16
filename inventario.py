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

    def mostrar_articulos(self):
        actual = self.primero
        while actual:
            print(f"articulo: {actual.dato}")
            actual = actual.siguiente

#aqui tambien se hacen las busquedas por lo que podemos usar la recursividad para encotrar el articulo