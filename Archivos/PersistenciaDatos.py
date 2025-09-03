import csv
from Clases_Base.Cliente import Cliente
from Clases_Base.Tarjeta import TarjetaDeCompra as Tarjeta
from Clases_Base.articulo import Articulo
from Clases_Base.Registro import Registro
from Estructuras.Carrodecompra import CarroDeCompra as Carrodecompra
from Estructuras.GestionRegistros import Registros
class Archivo:
    Clientes_csv = 'Archivos/Clientes.csv'
    Tarjetas_csv = 'Archivos/Tarjetas.csv'
    Articulos_csv = 'Archivos/Articulos.csv'
    Registros_csv = 'Archivos/Registros.csv'
    Carrodecompra_csv = 'Archivos/Carrodecompra.csv'

    @staticmethod
    def guardar_lista(objetos, path: str):
        if not objetos:
            return
        fieldnames = list(objetos[0].to_dict().keys())
        with open(path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for obj in objetos:
                writer.writerow(obj.to_dict())

    @staticmethod
    def cargar_lista(cls, path: str):
        objetos = []
        try:
            with open(path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    objetos.append(cls.from_dict(row))
        except FileNotFoundError:
            pass
        return objetos
    
    def guardar_clientes(clientes):
        Archivo.guardar_lista(clientes, Archivo.Clientes_csv)

    def cargar_clientes():
        return Archivo.cargar_lista(Cliente, Archivo.Clientes_csv)
    
    def guardar_tarjetas(tarjetas):
        Archivo.guardar_lista(tarjetas, Archivo.Tarjetas_csv)

    def cargar_tarjetas():
        return Archivo.cargar_lista(Tarjeta, Archivo.Tarjetas_csv)
    
    def guardar_articulos(articulos):
        Archivo.guardar_lista(articulos, Archivo.Articulos_csv)

    def cargar_articulos():
        return Archivo.cargar_lista(Articulo, Archivo.Articulos_csv)
    
    def guardar_carritos(carritos):
        fieldnames = ["id_carrito", "id_cliente", "id_producto","nombre","cantidad","precio_unitario","subtotal"]
        with open(Archivo.Carrodecompra_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for carrito in carritos:
                for item in carrito.Parametros_csv():
                    writer.writerow({
                        "id_carrito": carrito.id_carrito,
                        "id_cliente": carrito.cliente.id_cliente,
                        **item
                    })

    def cargar_carritos():
        carritos_dict = {}
        clientes = Archivo.cargar_clientes()
        try:
            with open(Archivo.Carrodecompra_csv, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    carrito_id = row["id_carrito"]
                    cliente_id = row["id_cliente"]
                    cliente = next((c for c in clientes if c.id_cliente == cliente_id), None)
                    if not cliente:
                        continue
                    if carrito_id not in carritos_dict:
                        carrito = Carrodecompra(cliente)
                        carrito.id_carrito = carrito_id
                        carritos_dict[carrito_id] = carrito
                    else:
                        carrito = carritos_dict[carrito_id]
                    
                    carrito.agregar_item(
                        id_producto=row["id_producto"],
                        nombre=row["nombre"],
                        cantidad=int(row["cantidad"]),
                        precio_unitario=float(row["precio_unitario"])
                    )
        except FileNotFoundError:
            pass
        return list(carritos_dict.values())
    
    def guardar_registros(registros):
        if isinstance(registros, Registros):
            lista = registros.lista_registros
        else:lista = registros
        Archivo.guardar_lista(lista, Archivo.Registros_csv)

    def cargar_registros():
        registros = []
        try:
            clientes = Archivo.cargar_clientes()
            carritos = Archivo.cargar_carritos()
            with open(Archivo.Registros_csv, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    registros.append(Registro.from_dict(row, clientes, carritos))
        except FileNotFoundError:
            pass
        return registros
    
    
    def guardar_datos(clientes, tarjetas, articulos, carritos, registros):
        Archivo.guardar_clientes(clientes)
        Archivo.guardar_tarjetas(tarjetas)
        Archivo.guardar_articulos(articulos)
        Archivo.guardar_carritos(carritos)
        Archivo.guardar_registros(registros)

    def cargar_datos():
        clientes = Archivo.cargar_clientes()
        tarjetas = Archivo.cargar_tarjetas()
        articulos = Archivo.cargar_articulos()
        carritos = Archivo.cargar_carritos()
        registros_lista=Archivo.cargar_registros()
        registros = Registros()
        registros.lista_registros = registros_lista
        return clientes, tarjetas, articulos, carritos, registros

