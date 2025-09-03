import os
from datetime import datetime

class ProcesarPago:
    #Procesos de pago y de facturacion
    def __init__(self, carro_de_compra):
        self.carro_de_compra = carro_de_compra

    def procesar_pago(self):
        print("Procesando pago...")
        self.carro_de_compra.pila_articulos()
        print("Pago procesado con éxito.")

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

