import csv

from Cliente import Cliente

class GestionClientes:
    def __init__(self, archivo_clientes):
        self.archivo_clientes = archivo_clientes
        self.clientes = []
        self.cargar_clientes()
        
    def cargar_clientes(self):
        self.clientes = []
        try:
            with open(self.archivo_clientes, newline='', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                for fila in lector:  
                    c = Cliente(fila[0], fila[1], fila[2])
                    self.clientes.append(c)
        except FileNotFoundError:
            with open(self.archivo_clientes, 'w', newline='', encoding='utf-8'):
                pass

    
    def guardar_clientes(self):
        with open(self.archivo_clientes, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            for c in self.clientes:
                escritor.writerow([c.nombre, c.id, c.password])


    def registrar_cliente(self, nombre, id, password):
        for c in self.clientes:
            if c.id == id:
                return False
        nuevo_cliente = Cliente(nombre, id, password)
        self.clientes.append(nuevo_cliente)
        self.guardar_clientes()
        return True

    def login(self, id, password):
        for c in self.clientes:
            if c.id == id and c.password == password:
                return c
        return None
    
    def eliminar_cliente(self, id, password):
        nueva_lista = [
            c for c in self.clientes
            if not (c.id == id and c.password == password)]
        if len(nueva_lista) == len(self.clientes):
            return False
        self.clientes = nueva_lista
        self.guardar_clientes()
        return True








