import csv
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
clases_base_path = os.path.join(current_dir, "Clases_Base")
sys.path.append(clases_base_path)
estructuras_path = os.path.join(current_dir, "Estructuras")
sys.path.append(estructuras_path)
Proyecto_Estructuras_Python_path= os.path.join(current_dir,"Proyecto_Estructuras_Python")
sys.path.append(Proyecto_Estructuras_Python_path)
from Clases_Base.articulo import Articulo
from Estructuras.inventario import ListaInventario

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


print("probando la busqueda recursiba por tipo")
articulo_tipo = lista.busqueda_recursiva("Muebles")
print(articulo_tipo)

print("probando el merge sort por precios")
lista_merge_sort = lista.merge_sort(lista_pila)
for nodo in lista_merge_sort:
    print(nodo.dato)
    print(nodo.pila)
    print(" -----------\n")

