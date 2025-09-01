import uuid
from Fechas import Tiempo
from Clases_Base import Cliente, CarritoDeCompra

class Registro:
    def _init_(self, cliente, carritoDeCompra, metodoDePago, estado="pendiente"):
        self.id_registro = str(uuid.uuid4())
        self.cliente = cliente
        self.carritoDeCompra = carritoDeCompra
        self.total=carritoDeCompra.calcular_total()
        self.metodoDePago = metodoDePago
        self.fecha=Tiempo.Ahora()
        self.estado = estado
    
    def _str_(self):
        return (f"Registro ID: {self.id_registro}\n"
                f"Cliente: {self.cliente.nombre} {self.cliente.apellido}\n"
                f"Carrito de Compra: {self.carritoDeCompra}\n"
                f"Total: ${self.total}\n"
                f"Método de Pago: {self.metodoDePago}\n"
                f"Estado: {self.estado}\n"
                f"Fecha: {Tiempo.obtener_fecha_hora_actual()}")
    
    def to_dict(self):
        return{
            "id_registro": self.id_registro,
            "id_cliente": self.cliente.id_cliente,
            "id_carrito": self.carritoDeCompra.id_carrito,
            "total":self.total,
            "metodoDePago": self.metodoDePago,
            "estado": self.estado,
            "fecha": self.fecha
        }
    
    @staticmethod
    def from_dict(data, clientes, carritos):
        #Este método busca el cliente según el id
        cliente= next((c for c in clientes if c.id_cliente == data["id_cliente"]), None)
        carrito= next((car for car in carritos if car.id_carrito == data["id_carrito"]), None)
        registro = Registro(
            cliente=cliente,
            carritoDeCompra=carrito,
            metodoDePago=data["metodoDePago"],
            estado=data["estado"]
        )
        registro.id_registro = data["id_registro"]
        registro.total = float(data["total"])
        registro.fecha = data["fecha"]
        return registro
