class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

#en primera instancia usariamos la lista para los inventarios de productos
class ListaInventarios:
    def __init__(self):
        self.primero = None

    def agregar_producto(self, producto):
        nuevo_nodo = Nodo(producto)
        if not self.primero:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_productos(self):
        actual = self.primero
        while actual:
            print(f"Producto: {actual.dato}")
            actual = actual.siguiente

#aqui tambien se hacen las busquedas por lo que podemos usar la recursividad para encotrar el producto