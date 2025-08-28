import csv
import datetime as dt

Clientes_csv = 'Estructura/clientes.csv'
Tarjetas_csv = 'Estructura/tarjetas.csv'
Articulos_csv = 'Estructura/articulos.csv'
Carritos_csv = 'Estructura/carritos.csv'
Registros_csv = 'Estructura/registros.csv'
from Clases_Base.cliente import Cliente
from Clases_Base.tarjeta import Tarjeta
from Clases_Base.articulo import Articulo
from Estructuras.Carrodecompra import CarroDeCompras
from Estructuras.Registro import Registros
#Cualquier cosa este documento está hecho muy separado cada función, ocupo investigar como hacerlo serializable después, posiblemente en estos días voy a modificarlo para que usarlo sea más cómodo
#Se utiliza path para definir la ruta del archivo CSV de mejor manera
def cargar_clientes(path: str=Clientes_csv)->list[Cliente]: #El str es para mejorar la legibilidad del documento
    clientes: list[Cliente] = [] 
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            if not reader.fieldnames:
                return []
            required = {'nombre','apellido','telefono','correo','direccion_envio','id_cliente','fecha_registro'}
            if not required.issubset(set(reader.fieldnames)):
                missing = required - set(reader.fieldnames)
                raise ValueError(f"Columnas faltantes en {path}:{missing}") #Esta parte verifica que las columnas necesarias estén en el archivo CSV
            for row in reader:
                try:
                    fecha = dt.datetime.strptime(row['fecha_registro'], '%Y-%m-%d').date()
                    cliente = Cliente(
                        nombre=row['nombre'],
                        apellido=row['apellido'],
                        telefono=row['telefono'],
                        correo=row['correo'],
                        direccion_envio=row['direccion_envio'],
                        id_cliente=int(row['id_cliente']),
                        fecha_registro=fecha
                    )
                    clientes.append(cliente)
                except ValueError as err:
                    print(f"Error al procesar la fila {row}:{err}")
    except FileNotFoundError:
        open(path, 'w', newline='', encoding='utf-8').close()
        return [] #Retorna una list avacía si el archivo no existe o si hubo un error con las personas
    return clientes

#Se haría lo mismo en el resto de funciones, obviamente quitamos fecha al ser solo una variable de Cliente
def cargar_tarjetas(path: str=Tarjetas_csv)->list[Tarjeta]:
    tarjetas: list[Tarjeta] = []
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            if not reader.fieldnames:
                return []
            required = {'numero_tarjeta','codigo','banco','id_usuario'}
            if not required.issubset(set(reader.fieldnames)):
                missing = required - set(reader.fieldnames)
                raise ValueError(f"Columnas faltantes en {path}:{missing}")
            for row in reader:
                try:
                    tarjeta = Tarjeta(
                        numero_tarjeta=row['numero_tarjeta'],
                        codigo=row['codigo'],
                        banco=row['banco'],
                        id_usuario=int(row['id_usuario'])
                    )
                    tarjetas.append(tarjeta)
                except ValueError as err:
                    print(f"Error al procesar la fila {row}:{err}")
    except FileNotFoundError:
        open(path, 'w', newline='', encoding='utf-8').close()
        return []
    return tarjetas

def cargar_articulos(path: str=Articulos_csv)->list[Articulo]:
    articulos: list[Articulo] = []
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            if not reader.fieldnames:
                return []
            required = {'nombre','tipo','precio','cantidad'}
            if not required.issubset(set(reader.fieldnames)):
                missing = required - set(reader.fieldnames)
                raise ValueError(f"Columnas faltantes en {path}:{missing}")
            for row in reader:
                try:
                    articulo = Articulo(
                        nombre=row['nombre'],
                        tipo=row['tipo'],
                        precio=float(row['precio']),
                        cantidad=int(row['cantidad'])
                    )
                    articulos.append(articulo)
                except ValueError as err:
                    print(f"Error al procesar la fila {row}:{err}")
    except FileNotFoundError:
        open(path, 'w', newline='', encoding='utf-8').close()
        return []
    return articulos

def cargar_carrito(path: str=Carritos_csv, clientes: list[Cliente]=[])->list[CarroDeCompras]:
    carritos: list[CarroDeCompras]=[]
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            if not reader.fieldnames:
                return []
            required = {'id_carrito','id_cliente','id_producto','nombre','cantidad','precio_unitario','subtotal'}
            if not required.issubset(set(reader.fieldnames)):
                missing = required - set(reader.fieldnames)
                raise ValueError(f"Columnas faltantes en {path}:{missing}")
            temporal_carritos = {}
            for row in reader:
                id_carrito = int(row['id_carrito'])
                id_cliente = int(row['id_cliente'])
                cliente = next((c for c in clientes if c.id_cliente == id_cliente), None)
                if not cliente:
                    continue #Aquí se omite ya que no existe el cliente
                if id_carrito not in temporal_carritos:
                    carrito = CarroDeCompras(cliente)
                    carrito.isntance.id_carrito = id_carrito
                    temporal_carritos[id_carrito] = carrito
                temporal_carritos[id_carrito].agregar_articulo(
                    id_producto=row['id_producto'],
                    nombre=row['nombre'],
                    cantidad=int(row['cantidad']),
                    precio_unitario=float(row['precio_unitario'])
                )
            carritos = list(temporal_carritos.values())
    except FileNotFoundError:
        open(path, 'w', newline='', encoding='utf-8').close()
        return []
    return carritos

#Esta clase registros tengo que revisarla bien aún, porque estoy viendo como hago bien los registros
def cargar_registros(path: str=Registros_csv)->list[Registros]:
    registros: list[Registros] = []
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            if not reader.fieldnames:
                return []
            required = {'tipo','usuario','id_carrito','id_cliente','fecha_creacion','total_carrito','id_producto','nombre_producto','cantidad','precio_unitario','subtotal'}
            if not required.issubset(set(reader.fieldnames)):
                missing = required - set(reader.fieldnames)
                raise ValueError(f"Columnas faltantes en {path}:{missing}")
            for row in reader:
                try:
                    cantidad=int(row['cantidad']) if row.get('cantidad') else None
                    precio_unitario=float(row['precio_unitario']) if row.get('precio_unitario') else None
                    subtotal=float(row['subtotal']) if row.get('subtotal') else None
                    registro = Registros(
                        tipo=row['tipo'],
                        usuario=row['usuario'],
                        id_carrito=row['id_carrito'],
                        id_producto=row['id_producto'],
                        nombre_producto=row['nombre_producto'],
                        cantidad=cantidad,
                        precio_unitario=precio_unitario,
                        subtotal=subtotal,
                        fecha=row['fecha_creacion'],
                    )
                    registros.append(registro)
                except ValueError as err:
                    print(f"Error al procesar la fila {row}:{err}")
    except FileNotFoundError:
        open(path, 'w', newline='', encoding='utf-8').close()
        return []
    return registros

def cargar_datos():
    clientes = cargar_clientes()
    tarjetas = cargar_tarjetas()
    articulos = cargar_articulos()
    carritos = cargar_carrito(clientes=clientes)
    #registros = cargar_registros() #Descomentar si se quiere usar registros
    return clientes, tarjetas, articulos, carritos