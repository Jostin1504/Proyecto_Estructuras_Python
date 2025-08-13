class ProcesarPago:
    #Procesos de pago y de facturacion
    def __init__(self, carro_de_compra):
        self.carro_de_compra = carro_de_compra

    def procesar_pago(self):
        print("Procesando pago...")
        self.carro_de_compra.pila_articulos()
        print("Pago procesado con éxito.")

#recordar que el primero se procesa el pago antes de eliminar los articulos por tema de no estar modificando el inventario

