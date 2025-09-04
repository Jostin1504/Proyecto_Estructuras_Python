import os
from datetime import datetime
from Clases_Base.Tarjeta import TarjetaDeCompra
from Clases_Base.Cliente import Cliente
from Estructuras.Carrodecompra import CarroDeCompra
from Archivos.PersistenciaDatos import Archivo as file
from Clases_Base.Registro import Registro
from Estructuras.GestionRegistros import Registros
class ProcesarPago:

    def __init__(self, carro_de_compra, gestor_tarjetas=None, gestor_registros = None):
        self.carro_de_compra = carro_de_compra
        self.gestor_tarjetas = gestor_tarjetas
        self.registros = gestor_registros

    def procesar_pago(self, cliente, numero_tarjeta, cvv, password):
        """Procesar pago con los datos recibidos"""
        
        if cliente.password != password:
            return "Contraseña incorrecta. Pago cancelado."
        
        tarjeta = None
        if self.gestor_tarjetas:
            for t in self.gestor_tarjetas.tarjetas:
                if t.numero_tarjeta == numero_tarjeta and t.codigo == cvv and t.id_usuario == cliente.id_cliente:
                    tarjeta = t
                    break

        if not tarjeta:
            return "Tarjeta no encontrada o datos incorrectos."

        total = self.carro_de_compra.calcular_total()
        if tarjeta.saldo < total:
            return f"Saldo insuficiente. Necesita ${total:.2f}, disponible ${tarjeta.saldo:.2f}"

        tarjeta.saldo -= total
        if self.gestor_tarjetas:
            file.guardar_tarjetas(self.gestor_tarjetas.tarjetas)

        registro = Registro(
            cliente=cliente,
            total=total,
            metodoDePago="Tarjeta",
            estado="Exitoso"
        )
        subtotal = registro.total
        iva = subtotal * 0.13
        total_con_iva = subtotal + iva
        lines = [
            "========= RECIBO DE COMPRA =========",
            f"Cliente: {registro.cliente.nombre} {registro.cliente.apellido}",
            f"Fecha: {registro.fecha}\n",
            f"Total: ${subtotal:.2f}",
            f"IVA (13%): {iva:.2f}",
            f"TOTAL A PAGAR: {total_con_iva:.2f}",
            f"Método de Pago: {registro.metodoDePago}",
            f"Estado: {registro.estado}",
            "=================================="
        ]
        registro.factura_texto = "\n".join(lines)

        self.registros.lista_registros.append(registro)
        file.guardar_registros(self.registros)
        print(f"Factura generada y guardada: {registro.id_registro}")

        return f"Pago realizado con éxito por ${total:.2f}"
