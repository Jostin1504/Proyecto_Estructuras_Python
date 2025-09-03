class Articulo:
    def __init__(self, nombre, tipo, precio, cantidad):
        if nombre == "" or tipo == "":
            raise ValueError("El nombre y el tipo no pueden estar vacíos.")
        else:
            self.nombre = nombre
            self.tipo = tipo
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        else:
            self.precio = precio
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        else:
            self.cantidad = cantidad

#esto muestra la info, sin esto solo muestra la direccion de memoria
    def __str__(self):
        return f" Articulo: {self.nombre}, Tipo: {self.tipo}, Precio: {self.precio}, Cantidad: {self.cantidad}"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "tipo": self.tipo,
            "precio": self.precio,
            "cantidad": self.cantidad
        }
    
    @staticmethod
    def from_dict(data):
        return Articulo(
            nombre=data["nombre"],
            tipo=data["tipo"],
            precio=float(data["precio"]),
            cantidad=int(data["cantidad"])
    )
