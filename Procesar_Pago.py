class ProcesarPago:
    #Procesos de pago y de facturacion
import os
from datetime import datetime
from Clases_Base.Tarjeta import TarjetaDeCompra
from Clases_Base.Cliente import Cliente


class ProcesarPago:

    def __init__(self, carro_de_compra, gestor_tarjetas=None):
        self.carro_de_compra = carro_de_compra
        self.gestor_tarjetas = gestor_tarjetas

    def procesar_pago(self, cliente, numero_tarjeta, cvv, password):
        """Procesar pago con los datos recibidos"""
        
        # Verificar contraseña del cliente
        if cliente.password != password:
            return "❌ Error: contraseña incorrecta. Pago cancelado."

        # Buscar tarjeta
        tarjeta = None
        if self.gestor_tarjetas:
            for t in self.gestor_tarjetas.tarjetas:
                if (t.numero_tarjeta == numero_tarjeta and 
                    t.codigo == cvv and 
                    t.id_usuario == cliente.id_cliente):
                    tarjeta = t
                    break

        if not tarjeta:
            return "❌ Tarjeta no encontrada o datos incorrectos."

        # Verificar saldo
        total = self.carro_de_compra.calcular_total()
        if tarjeta.saldo < total:
            return f"❌ Saldo insuficiente. Necesita ${total:.2f}, disponible ${tarjeta.saldo:.2f}"

        # Procesar pago
        tarjeta.saldo -= total
        self.generar_recibo()
        
        return f"✅ Pago realizado con éxito por ${total:.2f}"

    def generar_factura(self):
        carpeta = "Archivos/Recibos"
        os.makedirs(carpeta, exist_ok=True)

        nombre_archivo = f"recibo_{self.carro_de_compra.id_carrito}.txt"
        ruta = os.path.join(carpeta, nombre_archivo)

        subtotal = self.carro_de_compra.calcular_total()
        iva = subtotal * 0.13
        total = subtotal + iva 

        with open(ruta, "w", encoding="utf-8") as f:
            f.write("========= RECIBO DE COMPRA =========\n")
            f.write(f"Cliente: {self.carro_de_compra.cliente.nombre}\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            f.write("Artículos:\n")
            for item in self.carro_de_compra.items:
                f.write(f"- {item['nombre']} x{item['cantidad']} @ {item['precio_unitario']} = {item['subtotal']}\n")

            f.write("\n----------------------------------\n")
            f.write(f"Subtotal: {subtotal:.2f}\n")
            f.write(f"IVA (13%): {iva:.2f}\n")
            f.write(f"TOTAL A PAGAR: {total:.2f}\n")
            f.write("==================================\n")

        print(f"Factura generada en: {ruta}")

#recordar que el primero se procesa el pago antes de eliminar los articulos por tema de no estar modificando el inventario

