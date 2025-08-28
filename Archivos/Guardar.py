import csv
import datetime as dt

Clientes_csv = 'Estructura/clientes.csv'
Tarjetas_csv = 'Estructura/tarjetas.csv'
Articulos_csv = 'Estructura/articulos.csv'
Carritos_csv = 'Estructura/carritos.csv'
from Clases_Base.cliente import Cliente
from Clases_Base.tarjeta import Tarjeta
from Clases_Base.articulo import Articulo
from Estructuras.Carrodecompra import CarroDeCompras

#Lo hice similar al cargar, nada mas se revista la lista de cada cosa y se van guardando en el csv
def guardar_clientes(clientes: list[Cliente], path: str=Clientes_csv):
    fieldnames = ['nombre','apellido','telefono','correo','direccion_envio','id_cliente','fecha_registro']
    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for c in clientes:
            writer.writerow({
                'nombre': c.nombre,
                'apellido': c.apellido,
                'telefono': c.telefono,
                'correo': c.correo,
                'direccion_envio': c.direccion_envio,
                'id_cliente': c.id_cliente,
                'fecha_registro': c.fecha_registro.strftime('%Y-%m-%d')
            })

def guardar_tarjetas(tarjetas: list[Tarjeta], path: str=Tarjetas_csv):
    fieldnames = ['numero_tarjeta','codigo','banco','id_usuario']
    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for t in tarjetas:
            writer.writerow({
                'numero_tarjeta': t.numero_tarjeta,
                'codigo': t.codigo,
                'banco': t.banco,
                'id_usuario': t.id_usuario
            })

def guardar_articulos(articulos: list[Articulo], path: str=Articulos_csv):
    fieldnames = ['nombre','tipo','precio','cantidad']
    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for a in articulos:
            writer.writerow({
                'nombre': a.nombre,
                'tipo': a.tipo,
                'precio': a.precio,
                'cantidad': a.cantidad
            })

#El guardar carrito es algo más complejo, ya que hay que guardar el id del cliente y del carrito
def guardar_carritos(carritos: list[CarroDeCompras], path: str=Carritos_csv):
    fieldnames = ['id_carrito','id_cliente','id_producto','nombre','cantidad','precio_unitario','subtotal']
    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for c in carritos:
            for item in c.Parametros_csv():
                writer.writerow({
                    "id_carrito": c.id_carrito,
                    "id_cliente": c.cliente.id_cliente,
                    **item
                })

def guardar_datos(clientes: list[Cliente], tarjetas: list[Tarjeta], articulos: list[Articulo], carritos: list[CarroDeCompras]):
    guardar_clientes(clientes)
    guardar_tarjetas(tarjetas)
    guardar_articulos(articulos)
    guardar_carritos(carritos)