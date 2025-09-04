import csv
from Clases_Base.Cliente import Cliente
from Clases_Base.Tarjeta import TarjetaDeCompra as Tarjeta
from Clases_Base.articulo import Articulo
from Clases_Base.Registro import Registro
from Estructuras.Carrodecompra import CarroDeCompra as Carrodecompra
from Estructuras.GestionRegistros import Registros
class Archivo:
    Clientes_csv = 'Clientes.csv'
    Tarjetas_csv = 'Tarjetas.csv'
    Articulos_csv = 'Articulos.csv'
    Registros_csv = 'Registros.csv'

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
    
    def cargar_registros():
        registros = []
        try:
            clientes = Archivo.cargar_clientes()
            with open(Archivo.Registros_csv, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                if not reader.fieldnames or "id_cliente" not in reader.fieldnames or "id_registro" not in reader.fieldnames:
                    return []
                for row in reader:
                    if not row.get("id_registro") or not row.get("id_cliente"):
                        continue
                    try:
                        cliente = next((c for c in clientes if str(c.id_cliente) == str(row["id_cliente"])), None)
                        if not cliente:
                            print(f"Cliente con ID {row['id_cliente']} no encontrado para registro {row['id_registro']}")
                            continue
                        registro = Registro(
                            cliente=cliente,
                            total=float(row.get("total", 0.0)),
                            metodoDePago=row.get("metodo_de_pago", ""),
                            estado=row.get("estado", "pendiente")
                        )
                        registro.id_registro = row["id_registro"]
                        registro.fecha = row.get("fecha")  
                        registros.append(registro)
                    except Exception as e:
                        print(f"Advertencia al cargar registro {row.get('id_registro')}: {e}")
        except FileNotFoundError:
            pass
        return registros
    
    def guardar_registros(registros):
        if isinstance(registros, Registros):
            lista = registros.lista_registros
        else:lista = registros
        Archivo.guardar_lista(lista, Archivo.Registros_csv)

    def cargar_registros():
        registros = []
        try:
            clientes = Archivo.cargar_clientes()
            with open(Archivo.Registros_csv, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if not row.get("id_registro") or not row.get("id_cliente"):
                        continue
                    try:
                        registros.append(Registro.from_dict(row, clientes))
                    except ValueError as e:
                        print(f"Advertencia al cargar registro {row.get('id_registro')}: {e}")
        except FileNotFoundError:
            pass
        return registros
    
    
    def guardar_datos(clientes, tarjetas, articulos, registros):
        Archivo.guardar_clientes(clientes)
        Archivo.guardar_tarjetas(tarjetas)
        Archivo.guardar_articulos(articulos)
        Archivo.guardar_registros(registros)

    def cargar_datos():
        clientes = Archivo.cargar_clientes()
        tarjetas = Archivo.cargar_tarjetas()
        articulos = Archivo.cargar_articulos()
        registros_lista = Archivo.cargar_registros()
        registros = Registros()
        registros.lista_registros = registros_lista
        return clientes, tarjetas, articulos, registros

