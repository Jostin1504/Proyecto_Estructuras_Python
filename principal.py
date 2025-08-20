from articulo import Articulo
from inventario import ListaInventario

lista = ListaInventario()

lista.agregar_articulo(Articulo("Laptop", "Electrónica", 1500.00, 10))
lista.agregar_articulo(Articulo("Teléfono", "Electrónica", 800.00, 5))
lista.agregar_articulo(Articulo("Silla", "Muebles", 120.00, 20))
lista.agregar_articulo(Articulo("Mesa", "Muebles", 200.00, 15))
lista.agregar_articulo(Articulo("Libro", "Educación", 30.00, 50))
lista.mostrar_articulos()


print("Ordenando por cantidad...\n")
lista_pila = lista.pasar_a_lista_nodos(lista)
lista_ordenada_cantidad = lista.ordenarPorCantidad(lista_pila)

lista.mostrar_articulos()
