#La lista va a manejar pilas de articulos iguales
import csv
from Clases_Base.articulo import Articulo
class PilaArticulos:
    def __init__(self):
        self.items = []

    def apilar(self, items):
       self.items.append(items)

    def desapilar(self):
        #si no hay items
        if not self.items:
            return None
        #si, si hay
        return self.items.pop()
    
    def __str__(self):
        return f" Articulos apilados: {len(self.items)}"

class Nodo:
    def __init__(self, articulo):
        self.dato = articulo
        self.pila = PilaArticulos()  # Cada nodo tiene su propia pila de artículos
        #copia los articulos en la pila por la cantidad ingresada
        for _ in range(articulo.cantidad):
            self.pila.apilar(articulo)

        self.siguiente = None #ve la pila siguiente
        self.anterior = None  #ve la pila anterior
        
#lista doblemente enlazada para mas practicidad
class ListaInventario:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_articulo(self, articulo):
        """
        Agrega un artículo al inventario.
        Retorna True si se agrega exitosamente, False si ya existe.
        """
        # Verificar si el artículo ya existe
        if self.existe_articulo(articulo.nombre):
            return False  # El artículo ya existe
        
        nuevo_nodo = Nodo(articulo)
        if not self.primero:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo
        
        return True  # Artículo agregado exitosamente

    def existe_articulo(self, nombre):
        """
        Verifica si un artículo ya existe en el inventario.
        Retorna True si existe, False si no existe.
        """
        actual = self.primero
        while actual:
            if actual.dato.nombre.lower().strip() == nombre.lower().strip():
                return True
            actual = actual.siguiente
        return False

    #Clase basica para mostrar que es doble:
    def mostrar_articulos(self):
        actual = self.primero
        while actual:
            print(actual.dato)        
            print(actual.pila)        
            print(" -----------\n")
            actual = actual.siguiente

    #para que sirve este metodo?
    #debido a que se manejan pilas de articulos copia, este metodo permite obtener una lista de nodos
    #en otras palabras agarrar toda la pila
    @staticmethod
    def pasar_a_lista_nodos(lista_inventario):
        nodos = []
        actual = lista_inventario.primero
        while actual:
            nodos.append(actual)
            actual = actual.siguiente
        return nodos
    
    #metodos de ordenamiento selecction sort
    @staticmethod  #metodo para llamar sin instancia lo que seria un STATIC en c++
    def ordenarPorCantidad(lista_nodos):
        ordenada = []
        copia = lista_nodos[:] #copia la lista original
        while copia:
            menor = copia[0]
            for item in copia:
                if len(item.pila.items) < len(menor.pila.items): # Compara la can de articulos
                    menor = item
            ordenada.append(menor)
            copia.remove(menor)
        return ordenada

    @staticmethod
    def ordenarPorPrecios(lista_nodos):
        ordenada = []
        copia = lista_nodos[:]
        while copia:
            menor = copia[0]
            for item in copia:
                if item.dato.precio < menor.dato.precio:
                    menor = item
            ordenada.append(menor)
            copia.remove(menor)
        return ordenada

    @staticmethod
    def ordenarAlfabeticamente(lista_nodos):
        ordenada = []
        copia = lista_nodos[:]
        while copia:
            menor = copia[0]
            for item in copia:
                if item.dato.nombre.lower() < menor.dato.nombre.lower():
                    menor = item
            ordenada.append(menor)
            copia.remove(menor)
        return ordenada

    #metodo de busqueda
    def buscar_articulo_nombre(self, nombre):
        actual = self.primero
        while actual:
            if actual.dato.nombre.lower() == nombre.lower():
                return actual.pila
            actual = actual.siguiente
        return None
    
    def buscar_articulo_tipo(self, tipo):
        actual = self.primero
        while actual:
            if actual.dato.tipo.lower() == tipo.lower():
                return actual.dato
            actual = actual.siguiente
        return None
    
    #este metodo esta hecho para que solo elimine despues de completar con exito la compra
    def eliminar_articulo(self, nombre, cantidad=None):
        """
        Elimina un artículo del inventario.
        Si no se especifica cantidad, elimina el nodo completo.
        Si se especifica cantidad, elimina esa cantidad de la pila.
        Retorna True si se elimina exitosamente, False si no se encuentra.
        """
        actual = self.primero
        while actual:
            if actual.dato.nombre.lower().strip() == nombre.lower().strip():
                if cantidad is None:
                    # Eliminar nodo completo
                    if actual.anterior:
                        actual.anterior.siguiente = actual.siguiente
                    else:
                        self.primero = actual.siguiente
                    
                    if actual.siguiente:
                        actual.siguiente.anterior = actual.anterior
                    else:
                        self.ultimo = actual.anterior
                    
                    return True
                else:
                    # Eliminar cantidad específica
                    for _ in range(min(cantidad, len(actual.pila.items))):
                        actual.pila.desapilar()
                    
                    if not actual.pila.items:
                        # Si la pila está vacía, eliminar el nodo
                        if actual.anterior:
                            actual.anterior.siguiente = actual.siguiente
                        else:
                            self.primero = actual.siguiente
                        
                        if actual.siguiente:
                            actual.siguiente.anterior = actual.anterior
                        else:
                            self.ultimo = actual.anterior
                    
                    return True
            actual = actual.siguiente
        return False
    
    def eliminar_uno(self, nombre):
        actual = self.primero
        if not self.verificar_cantidad_articulo(nombre, 1):
            print("No hay suficientes artículos en la pila.")
            return False
        else:
            while actual:
                if actual.dato.nombre.lower() == nombre.lower():
                    actual.pila.desapilar()
                    if not actual.pila.items:
                        if actual.anterior:
                            actual.anterior.siguiente = actual.siguiente
                        else:
                            self.primero = actual.siguiente
                        if actual.siguiente:
                            actual.siguiente.anterior = actual.anterior
                        else:
                            self.ultimo = actual.anterior
                    return True
                actual = actual.siguiente
        return False

    #Este metodo comprueba la cantidad de la pila para evitar que el usuario 
    #intente comprar mas de los que hay 
    def verificar_cantidad_articulo(self, nombre, cantidad):
        actual = self.primero
        while actual:
            if actual.dato.nombre.lower() == nombre.lower():
                return len(actual.pila.items) >= cantidad
            actual = actual.siguiente
        return False
    

    #guardar y cargar csv
    def guardar_inventario(self, nombre_archivo ="inventario.csv"):
        print("Entre en guardar")
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Pila: ", "Nombre: ", "Tipo: ", "Precio: ", "Cantidad: ","\n"])
            actual = self.primero
            contador = 1

            while actual:
                fila = [f"\nPila {contador}", actual.dato.nombre, actual.dato.tipo, actual.dato.precio]

                for i, pila in enumerate(actual.pila.items, start=1):
                    obj = [str(obj) for obj in pila.items]
                    escritor.writerow([f"Pila {i}"] + obj)
                contador += 1
                actual = actual.siguiente

    def cargar_inventario(self, nombre_archivo="inventario.csv"):
        print("Entre en cargar")
        with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Saltos de linea

            for fila in lector:
                #acomoda por filas
                nombre = fila[1]
                tipo = fila[2]
                precio = float(fila[3])
                cantidad = int(fila[4])
                articulo_obj = Articulo(nombre, tipo, precio, cantidad) #crea nuevamente el objeto Articulo
                self.agregar_articulo(articulo_obj)                     #lo agrega a la lista
                print(f"Cargado: {fila}")