import csv
from datetime import dt #Esta clase perite trabajar con fechas de mejor manera sin errores pero hay que saber la estructura digamos xd
from Estructuras.Carrodecompra import CarroDeCompras
Registros_csv = 'Estructura/registros.csv'

class Registros:
    def __init__(self, path: str=Registros_csv):
        self.path = path
        self.registros = []

    def agregar_accion(self, usuario, accion):
        registro = {
            'tipo:': 'accion',
            'usuario': usuario,
            'accion': accion,
            'fecha_hora': dt.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.registros.append(registro)
        
    def agregar_compra(self, carrito: CarroDeCompras):
        for item in carrito.Parametros_csv():
            registro = {
                "tipo": "compra",
                "usuario": carrito.cliente.nombre,
                "id_carrito": carrito.id_carrito,
                "id_cliente": carrito.cliente.id_cliente,
                "fecha_creacion": carrito.fecha_creacion,
                "total_carrito": carrito.total_carrito,
                "id_producto": item['id_articulo'],
                "nombre_producto": item['nombre'],
                "cantidad": item['cantidad'],
                "precio_unitario": item['precio'],
                "subtotal": item['subtotal']
            }
            self.registros.append(registro)
    def listar_registros(self, tipo=None):
        return self.registros 