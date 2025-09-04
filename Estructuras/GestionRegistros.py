from Clases_Base.Registro import Registro

class Registros:
    def __init__(self):
        self.lista_registros = []

    def agregar_registro(self, cliente, total, metodo_pago, estado="pendiente"):
        registro = Registro(cliente, total, metodo_pago, estado)
        self.lista_registros.append(registro)

        if not hasattr(cliente, "Historial_compras"):
            cliente.Historial_compras = []
        cliente.Historial_compras.append(registro.id_registro)

        return registro

    def buscar_por_id(self, id_registro):
        return next((r for r in self.lista_registros if r.id_registro == id_registro), None)

    def buscar_por_cliente(self, cliente_id):
        return [r for r in self.lista_registros if r.cliente.id_cliente == cliente_id]

    def listar_registros(self):
        return self.lista_registros

    def actualizar_estado(self, id_registro, nuevo_estado):
        registro = self.buscar_por_id(id_registro)
        if registro:
            registro.estado = nuevo_estado
            return True
        return False

    def cantidad_registros(self):
        return len(self.lista_registros)

    def __str__(self):
        return f"Registros: {self.cantidad_registros()}"
