#Una composicion de las tarjetas con el usuario
class TarjetaDeCompra:
    def __init__(self, numero_tarjeta, codigo, banco, id_usuario):
        self.numero_tarjeta = numero_tarjeta
        self.codigo = codigo
        self.banco = banco
        self.id_usuario = id_usuario
        self.saldo = 0.0
        self.maximo_saldo = 3000.0
        self.recargas_realizadas = {200:0,400:0,800:0,1000:0}

    def info_tarjeta(self):
        print(f"Tarjeta: {self.numero_tarjeta}")
        print(f"Banco: {self.banco}")
        print(f"Saldo: {self.saldo}")

    def puede_recargar(self, monto):
        return self.saldo + monto <= self.maximo_saldo

    def recargar(self, monto):
        if self.puede_recargar(monto):
            self.saldo += monto
            return True
        return False
    
    def to_dict(self):
        recargas_str = ":".join([f"{k}:{v}" for k, v in self.recargas_realizadas.items()])
        return {
            "numero_tarjeta": self.numero_tarjeta,
            "codigo": self.codigo,
            "banco": self.banco,
            "id_usuario": self.id_usuario,
            "saldo": self.saldo,
        }
    
    @staticmethod
    def from_dict(data):
        tarjeta=TarjetaDeCompra(
            numero_tarjeta=data["numero_tarjeta"],
            codigo=data["codigo"],
            banco=data["banco"],
            id_usuario=data["id_usuario"]
        )
        tarjeta.saldo = float(data["saldo"])
        recargas_str = data.get("recargas_realizadas","")
        if isinstance(recargas_str,str):
            recargas_dict={}
            if recargas_str:
                for recargas in recargas_str.split(";"):
                    try:
                        k, v, *_ = recargas.split(":")
                        recargas_dict[int(k)] = int(v)
                    except Exception:
                        print(f"Ignorando recarga inválida: {recargas}")
        if not recargas_dict:
            recargas_dict={200:0,400:0,800:0,1000:0}

        tarjeta.recargas_realizadas = recargas_dict
        return tarjeta
    
    def __str__(self):
        return (f"Tarjeta Número: {self.numero_tarjeta}\n"
                f"Banco: {self.banco}\n"
                f"Saldo: ${self.saldo}\n"
        )
