#Una composicion de las tarjetas con el usuario
class TarjetaDeCompra:
    def __init__(self, numero_tarjeta, codigo, banco, id_usuario, saldo = 0):
        self.numero_tarjeta = numero_tarjeta
        self.codigo = codigo
        self.banco = banco
        self.id_usuario = id_usuario
        self.saldo = saldo

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
            "saldo": self.saldo
        }
    
    @staticmethod
    def from_dict(data):
        tarjeta = TarjetaDeCompra(
            numero_tarjeta=data["numero_tarjeta"],
            codigo=data["codigo"],
            banco=data["banco"],
            id_usuario=data["id_usuario"],
            saldo=data["saldo"]
        )
        return tarjeta
    
    def __str__(self):
        return (f"Tarjeta Número: {self.numero_tarjeta}\n"
                f"Banco: {self.banco}\n"
                f"Saldo: ${self.saldo}\n")