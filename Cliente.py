import csv
import uuid #Sirve para crear un ID unico, podriamos usarlo como que cada cliente tenga uno, al igual que en la comprar y transacciones.
from datetime import datetime,timedelta, timezone #timezone nos sirve por si en alguna ocasion llegan a realizar comprar internacionales.
from Fechas import Tiempo
from Tarjetas import TarjetaDeCompra
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
        self.tarjetas_compra=[] #lista de tarjetas registradas

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
    def agregar_tarjeta(self,numero_tarjeta,codigo, banco):
        tarjeta=TarjetaDeCompra(numero_tarjeta,codigo,banco)
        self.tarjetas_compra.append(tarjeta)
        print(f"Tarjeta {numero_tarjeta}vinculada al cliente {self.nombre+" "+self.apellido}({self.id_Cliente})")    
    def mostrar_tarjetas(self):
        if not self.tarjetas_compra:
         print(f"El cliente no tiene tarjetas registradas")
        else: 
            print(f"Tarjetas de {self.nombre}:")
            for t in self.tarjetas_compra:
             t.info_tarjeta(t)    
    def eliminar_tarjetas(self,numero_tarjeta):
        for t in self.tarjetas_compra:
            if t.numero_tarjeta==numero_tarjeta:
                self.tarjetas_compra.remove(t)
                print(f"Tarjeta {numero_tarjeta}eliminada del cliente {self.nombre}")
            else: 
                print(f"No se encontro la tarjeta {numero_tarjeta}  en el cliente {self.nombre}")              

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

