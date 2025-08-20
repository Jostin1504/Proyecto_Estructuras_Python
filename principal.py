from articulo import Articulo
from inventario import ListaInventario

lista = ListaInventario()

lista.agregar_articulo(Articulo("Laptop", "Electrónica", 1500.00, 10))
lista.agregar_articulo(Articulo("Teléfono", "Electrónica", 800.00, 5))
lista.agregar_articulo(Articulo("Silla", "Muebles", 120.00, 20))
lista.agregar_articulo(Articulo("Mesa", "Muebles", 200.00, 15))
lista.agregar_articulo(Articulo("Libro", "Educación", 30.00, 50))
lista.agregar_articulo(Articulo("Cámara", "Fotografía", 600.00, 7))
print("Lista original:")
lista.mostrar_articulos()

print("Buscando artículo por nombre: ")
pilabusqueda = lista.buscar_articulo_nombre("Laptop")
print(pilabusqueda)


print("Ordenando por cantidad...\n")
lista_pila = lista.pasar_a_lista_nodos(lista)
lista_ordenada_cantidad = lista.ordenarPorCantidad(lista_pila)

#esto muestra la lista ordenada
for nodo in lista_ordenada_cantidad:
    print(nodo.dato)   #muestra el articulo
    print(nodo.pila)   #muestra la pila
    print(" -----------\n")

print("Eliminando un artículo de la pila...")
lista.eliminar_articulo("Laptop", 8)
print(pilabusqueda)

print("Ordenando por precios...\n")
lista_ordenada_precios = lista.ordenarPorPrecios(lista_pila)
for nodo in lista_ordenada_precios:
    print(nodo.dato)
    print(nodo.pila)   
    print(" -----------\n")

print("Ordenando alfabéticamente por Articulo...\n")
lista_ordenada_alfabeticamente = lista.ordenarAlfabeticamente(lista_pila)
for nodo in lista_ordenada_alfabeticamente:
    print(nodo.dato)
    print(nodo.pila)
    print(" -----------\n")


