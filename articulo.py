class Articulo:
    def __init__(self, nombre, tipo, precio, cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.cantidad = cantidad

    def info_articulo(self):
        print(f"Articulo: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad: {self.cantidad}")
