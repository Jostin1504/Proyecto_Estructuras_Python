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

    def to_dict(self):
        return {
            "numero_tarjeta": self.numero_tarjeta,
            "codigo": self.codigo,
            "banco": self.banco,
            "id_usuario": self.id_usuario,
            "saldo": self.saldo,
            "recargas_realizadas": self.recargas_realizadas
        }
    
    @staticmethod
    def from_dict(data):
        tarjeta = TarjetaDeCompra(
            numero_tarjeta=data["numero_tarjeta"],
            codigo=data["codigo"],
            banco=data["banco"],
            id_usuario=data["id_usuario"]
        )
        tarjeta.saldo = data["saldo"]
        tarjeta.recargas_realizadas = data["recargas_realizadas"]
        return tarjeta
    
    def __str__(self):
        return (f"Tarjeta Número: {self.numero_tarjeta}\n"
                f"Banco: {self.banco}\n"
                f"Saldo: ${self.saldo}\n"
                f"Recargas Realizadas: {self.recargas_realizadas}")
    
    
