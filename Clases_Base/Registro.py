import uuid
from Fechas import Tiempo
from Clases_Base import Cliente
from Estructuras.Carrodecompra import CarroDeCompra
class Registro:
    def __init__(self, cliente, carritoDeCompra, metodoDePago, estado="pendiente"):
        self.id_registro = str(uuid.uuid4())
        self.cliente = cliente
        self.carritoDeCompra = carritoDeCompra
        self.total=carritoDeCompra.calcular_total()
        self.metodoDePago = metodoDePago
        self.fecha=Tiempo.Ahora()
        self.estado = estado
    
    def __str__(self):
        return (f"Registro ID: {self.id_registro}\n"
                f"Cliente: {self.cliente.nombre} {self.cliente.apellido}\n"
                f"Carrito de Compra: {self.carritoDeCompra}\n"
                f"Total: ${self.total}\n"
                f"Método de Pago: {self.metodoDePago}\n"
                f"Estado: {self.estado}\n"
                f"Fecha: {Tiempo.Ahora}")
    
    def to_dict(self):
        return {
            "id_registro": self.id_registro,
            "id_cliente": self.cliente.id_cliente,
            "id_carrito": self.carritoDeCompra.id_carrito,
            "total": self.total,
            "metodo_de_pago": self.metodoDePago,
            "fecha": str(self.fecha),
            "estado": self.estado
        }

    @staticmethod
    def from_dict(data, clientes, carritos):
        #Esto lo que hace es buscar el cliente y carrito por medio del ID para poder cargarlos, nunca se debe cargar un registro sin haber cargado los clientes y/o carritos
        id_cliente = data["id_cliente"]
        cliente = next((c for c in clientes if str(c.id_cliente) == str(id_cliente)), None)
        if cliente is None:
            raise ValueError(f"Cliente con ID {id_cliente} no encontrado.")
        id_carrito = data["id_carrito"]
        carrito = next((c for c in carritos if str(c.id_carrito) == str(id_carrito)), None)
        if carrito is None:
            raise ValueError(f"Carrito con ID {id_carrito} no encontrado.")
        registro = Registro(
            cliente=cliente,
            carritoDeCompra=carrito,
            metodoDePago=data.get("metodo_de_pago"),
            estado=data.get("estado", "pendiente")
        )
        registro.id_registro = data["id_registro"]
        registro.total = float(data["total"])
        registro.fecha = data["fecha"]
        return registro
