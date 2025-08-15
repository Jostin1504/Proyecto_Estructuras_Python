import csv
import uuid #Sirve para crear un ID unico, podriamos usarlo como que cada cliente tenga uno, al igual que en la comprar y transacciones.
from datetime import datetime,timedelta, timezone #timezone nos sirve por si en alguna ocasion llegan a realizar comprar internacionales.
class Cliente:
    def __init__(self, nombre, apellido, telefono, correo, direccion_envio,id_Cliente,fecha_registro):
        self.nombre = nombre
        self.apellido=apellido
        self.telefono=telefono
        self.correo=correo
        self.direccion_envio=direccion_envio
        self.id_Cliente=id_Cliente
        self.fecha_registro=fecha_registro
        self.Historial_compras=[] #Puede ser para ver el carrito de compras
    def info_cliente(self):
        print(f"Cliente: {self.nombre}({self.id_Cliente})")
        print(f"Apellido{self.apellido}")
        print(f"Telefono:{self.telefono}")
        print(f"Correo: {self.correo}")
        print(f"direccion_envio{self.direccion_envio}")
        print(f"fecha_registro{self.fecha_registro}")
    def parametros(self):
        return{
            "id_Cliente":self.id_Cliente,
            "nombre":self.nombre,
            "Apellido":self.apellido,
            "correo":self.correo,
            "Telefono":self.telefono,
            "direccion_envio":self.direccion_envio,
            "fecha_registro":self.fecha_registro
        }    
    def fecha_de_registro(self):
        self.fecha_registro=Tiempo()

    @staticmethod
    def parametros_data(data):
        cliente=Cliente(
            nombre=data["nombre"],
            apellido=data["apellido"],
            telefono=data["telefono"],
            correo=data["correo"],
            direccion_envio=data["direccion_envio"],
            id_Cliente=data["id_Cliente"]
        )
        cliente.fecha_registro = Tiempo.from_string(data["fecha_registro"])
        cliente.historial_compras = data["historial_compras"].split(";") if data["historial_compras"] else []
        return cliente

    def solicitar_servicio(self, servicio):
        print(f"{self.nombre} ha solicitado el servicio de {servicio}.")


#en primera instancia con los clientes se usaria la cola
#el primero que se hace siempre queda de primero en el proceso de pago