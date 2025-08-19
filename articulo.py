class Articulo:
    def __init__(self, nombre, tipo, precio, cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.cantidad = cantidad

#esto muestra la info, sin esto solo muestra la direccion de memoria
    def __str__(self):
        return f" Articulo: {self.nombre}, Tipo: {self.tipo}, Precio: {self.precio}, Cantidad: {self.cantidad}"