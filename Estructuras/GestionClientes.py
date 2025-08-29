import csv
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
clases_base_path = os.path.join(current_dir, "Clases_Base")
sys.path.append(clases_base_path)
from Clases_Base.Cliente import Cliente
#Si quiere agrega la clase Cargar y Guardar en vez de hacerlo de manera local
class GestionClientes:
    def __init__(self, archivo_clientes):
        self.archivo_clientes = archivo_clientes
        self.clientes = []
        self.cargar_clientes()
        
    def cargar_clientes(self):
        self.clientes = []
        try:
            with open(self.archivo_clientes, newline='', encoding='utf-8') as archivo:
                reader = csv.reader(archivo)
                for fila in reader:  
                    c = Cliente(fila[0], fila[1], fila[2])
                    self.clientes.append(c)
        except FileNotFoundError:
            with open(self.archivo_clientes, 'w', newline='', encoding='utf-8'):
                pass

    def guardar_clientes(self):
        #self.clientes=cargar_clientes(self.archivo_clientes) creo que sería para llamarlo
        with open(self.archivo_clientes, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            for c in self.clientes:
                escritor.writerow([c.nombre, c.id, c.password])

    def registrar_cliente(self, nombre, id ,password,apellido,telefono, correo, direccion_envio,fecha_registro):
        for c in self.clientes:
            if c.id_cliente== id:
                return False
        nuevo_cliente = Cliente(nombre, apellido, telefono, correo, direccion_envio, id, fecha_registro, password)
        self.clientes.append(nuevo_cliente)
        self.guardar_clientes()
        return True

    def login(self, id, password):
        for c in self.clientes:
            if c.id == id and c.password == password:
                return c
        return None
    
    def eliminar_cliente(self, id, password):
        for c in self.clientes:
            if c.id == id and c.password == password:
                self.clientes.remove(c)
                self.guardar_clientes()
                return True
        return False








