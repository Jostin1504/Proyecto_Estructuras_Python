#Una composicion de las tarjetas con el usuario
class TarjetaDeCompra:
    def __init__(self, numero_tarjeta, codigo, banco, id_usuario):
        self.numero_tarjeta = numero_tarjeta
        self.codigo = codigo
        self.banco = banco
        self.id_usuario = id_usuario
        self.saldo = 0.0
        self.recargas_realizadas = {200: 0, 400: 0, 800: 0, 1000: 0}

    def info_tarjeta(self):
        print(f"Tarjeta: {self.numero_tarjeta}")
        print(f"Banco: {self.banco}")
        print(f"Saldo: {self.saldo}")



    
    