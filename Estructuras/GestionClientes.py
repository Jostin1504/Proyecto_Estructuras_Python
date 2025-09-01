import csv
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
clases_base_path = os.path.join(current_dir, "Clases_Base")
sys.path.append(clases_base_path)
from Clases_Base.Cliente import Cliente

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
                    if len(fila) >= 8:  
                        c = Cliente(
                            nombre=fila[0],
                            apellido=fila[3], 
                            telefono=fila[4],
                            correo=fila[5],
                            direccion_envio=fila[6],
                            id_cliente=fila[1],  
                            fecha_registro=fila[7],
                            password=fila[2]
                        )
                        self.clientes.append(c)
        except FileNotFoundError:
            with open(self.archivo_clientes, 'w', newline='', encoding='utf-8'):
                pass
 
    def guardar_clientes(self):
        with open(self.archivo_clientes, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            for c in self.clientes:
                
                escritor.writerow([
                    c.nombre, 
                    c.id_cliente,  
                    c.password,
                    c.apellido,
                    c.telefono,
                    c.correo,
                    c.direccion_envio,
                    c.fecha_registro
                ])
 
    def registrar_cliente(self, nombre, id, password, apellido, telefono, correo, direccion_envio, fecha_registro):
        
        for c in self.clientes:
            if c.id_cliente == id:  
                return False
        
        nuevo_cliente = Cliente(
            nombre=nombre, 
            apellido=apellido, 
            telefono=telefono, 
            correo=correo, 
            direccion_envio=direccion_envio, 
            id_cliente=id, 
            fecha_registro=fecha_registro, 
            password=password
        )
        self.clientes.append(nuevo_cliente)
        self.guardar_clientes()
        return True
    
    def login(self, id, password):
        for c in self.clientes:
            if c.id_cliente == id and c.password == password:
                return c
        return None
         
    def eliminar_cliente(self, id, password):
        for c in self.clientes:
            if c.id_cliente == id and c.password == password:
                self.clientes.remove(c)
                self.guardar_clientes()
                return True
        return False







