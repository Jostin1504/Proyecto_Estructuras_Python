from articulo import Articulo
from inventario import ListaInventario

lista = ListaInventario()

lista.agregar_articulo(Articulo("Laptop", "Electrónica", 1500.00, 10))
lista.agregar_articulo(Articulo("Teléfono", "Electrónica", 800.00, 5))
lista.agregar_articulo(Articulo("Silla", "Muebles", 120.00, 20))

lista.mostrar_articulos()

