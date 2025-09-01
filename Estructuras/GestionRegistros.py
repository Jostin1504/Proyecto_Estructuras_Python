from Clases_base.Registro import Registro

class Registros:
    def _init_(self):
        self.lista_registros = []

    def agregar_registro(self, cliente, carrito, metodo_pago, estado):
        registro = Registro(cliente, carrito, metodo_pago, estado)
        self.lista_registros.append(registro)
        cliente.Historial_compras.append(registro.id_registro)
        return registro
    
    def buscar_por_id(self, id_registro):
        for registro in self.lista_registros:
            if registro.id_registro == id_registro:
                return registro
        return None
    
    def buscar_por_clientes(self, cliente_id):
        return [registro for registro in self.lista_registros if registro.cliente.id_cliente == cliente_id]
    
    def listar_registros(self):
        return self.lista_registros
    
    def actualizar_estado(self, id_registro, nuevo_estado):
        registro = self.buscar_por_id(id_registro)
        if registro:
            registro.estado = nuevo_estado
            return True
        return False
