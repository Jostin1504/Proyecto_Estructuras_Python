#posible main aunque no se ocupe pero por costumbre y para ir probando lo que se tiene tambien
from articulo import Articulo
from inventario import ListaInventario

inventario1 = ListaInventario()

articulo1 = Articulo("Camisa", "Ropa", 19.99, 50)
articulo2 = Articulo("TV", "Electrónica", 500.99, 30)

inventario1.agregar_articulo(articulo1)
inventario1.agregar_articulo(articulo2)

