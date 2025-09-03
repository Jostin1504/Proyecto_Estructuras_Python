import csv
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
clases_base_path = os.path.join(current_dir, "Clases_Base")
sys.path.append(clases_base_path)
estructuras_path = os.path.join(current_dir, "Estructuras")
sys.path.append(estructuras_path)
Proyecto_Estructuras_Python_path= os.path.join(current_dir,"Proyecto_Estructuras_Python")
sys.path.append(Proyecto_Estructuras_Python_path)
from Clases_Base.Tarjeta import TarjetaDeCompra
from Clases_Base.Cliente import Cliente
from GestionClientes import GestionClientes
from Archivos.PersistenciaDatos import Archivo as file

class GestionTarjetas:
    def __init__(self, archivo_tarjetas, gestor_clientes):
        self.archivo_tarjetas = archivo_tarjetas
        self.gestor_clientes = gestor_clientes
        self.tarjetas = []
        self.cargar_tarjetas()
        #esto es para restringir las recargas posibles por monto
    def cargar_tarjetas(self):
        self.tarjetas = file.cargar_tarjetas()

    def guardar_tarjetas(self):
        file.guardar_tarjetas(self.tarjetas)

    def registrar_tarjeta(self, id_usuario, numero, codigo, banco):
       if len(numero) not in (15, 16):
         raise ValueError(f"Número de tarjeta inválido: {numero}")
       if len(codigo) != 3:
         raise ValueError(f"Código de seguridad inválido: {codigo}")
     
    # CORREGIDO: Buscar cliente por ID directamente (con conversión de tipos)
       cliente = None
       for c in self.gestor_clientes.clientes:
        # Comparar tanto como string como valor original por si hay diferencias de tipo
         if str(c.id_cliente).strip() == str(id_usuario).strip():
             cliente = c
             break
    
       if not cliente:
        raise ValueError(f"No existe el cliente con id '{id_usuario}'")
    
       tarjeta = TarjetaDeCompra(numero, codigo, banco, id_usuario)
       self.tarjetas.append(tarjeta)
    
    # Agregar tarjeta a la lista del cliente si tiene esa propiedad
       if hasattr(cliente, 'tarjetas'):
          cliente.tarjetas.append(tarjeta)
       elif hasattr(cliente, 'tarjetas_compra'):
          cliente.tarjetas_compra.append(tarjeta)
    
       self.guardar_tarjetas()
       return True

    def autenticar_tarjeta(self, numero, codigo):
        for t in self.tarjetas:
            if t.numero_tarjeta == numero and t.codigo == codigo:
                return t
        return None

    def eliminar_tarjeta(self, id_usuario, numero, codigo):
        cliente = self.gestor_clientes.login(id_usuario, None)
        if not cliente:
            raise ValueError(f"No existe el cliente con id '{id_usuario}'")
        tarjeta = next(
            (t for t in self.tarjetas
             if t.numero_tarjeta == numero and t.codigo == codigo and t.id_usuario == id_usuario),
            None
        )
        if not tarjeta:
            return False
        self.tarjetas.remove(tarjeta)
        cliente.tarjetas.remove(tarjeta)
        self.guardar_tarjetas()
        return True
    
    #para la recarga de tarjetas
    def recargar_tarjeta(self, tarjeta, monto):
        if monto <= 0:
            raise ValueError("El monto de recarga debe ser positivo.")
        
        if monto > 3000:
            raise ValueError("El monto de recarga no puede exceder los $3000.")
   
        if not tarjeta.puede_recargar(monto):
           saldo_disponible = tarjeta.maximo_saldo - tarjeta.saldo
           raise ValueError("No se puede recargar. Saldo máximo alcanzado.")

        if tarjeta.recargar(monto):
            self.guardar_tarjetas()
            return f"Recarga de ${monto} exitosa. Nuevo saldo: ${tarjeta.saldo}"
        else:
            raise ValueError("No se pudo realizar la recarga.")
        
        