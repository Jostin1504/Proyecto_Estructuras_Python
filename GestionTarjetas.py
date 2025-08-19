import csv
from Tarjeta import TarjetaDeCompra
from Cliente import Cliente
from GestionClientes import GestionClientes

class GestionTarjetas:
    def __init__(self, archivo_tarjetas, gestor_clientes):
        self.archivo_tarjetas = archivo_tarjetas
        self.gestor_clientes = gestor_clientes
        self.tarjetas = []
        self.cargar_tarjetas()

    def cargar_tarjetas(self):
        self.tarjetas = []
        try:
            with open(self.archivo_tarjetas, newline='', encoding='utf-8') as f:
                lector = csv.reader(f)
                for num, cvv, banco, id_usuario in lector:
                    tarjeta = TarjetaDeCompra(num, cvv, banco, id_usuario)
                    self.tarjetas.append(tarjeta)
                    cliente = self.gestor_clientes.login(id_usuario, None)
                    if cliente:
                        cliente.tarjetas.append(tarjeta)
        except FileNotFoundError:
            open(self.archivo_tarjetas, 'w', encoding='utf-8').close()

    def guardar_tarjetas(self):
        with open(self.archivo_tarjetas, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            for t in self.tarjetas:
                escritor.writerow([t.numero, t.codigo, t.banco, t.id_usuario])

    def registrar_tarjeta(self, id_usuario, numero, codigo, banco):
        if len(numero) not in (15, 16):
            raise ValueError(f"Número de tarjeta inválido: {numero}")
        if len(codigo) != 3:
            raise ValueError(f"Código de seguridad inválido: {codigo}")
        cliente = self.gestor_clientes.login(id_usuario, None)
        if not cliente:
            raise ValueError(f"No existe el cliente con id '{id_usuario}'")
        tarjeta = TarjetaDeCompra(numero, codigo, banco, id_usuario)
        self.tarjetas.append(tarjeta)
        cliente.tarjetas.append(tarjeta)
        self.guardar_tarjetas()
        return True

    def autenticar_tarjeta(self, numero, codigo):
        for t in self.tarjetas:
            if t.numero == numero and t.codigo == codigo:
                return t
        return None

    def eliminar_tarjeta(self, id_usuario, numero, codigo):
        cliente = self.gestor_clientes.login(id_usuario, None)
        if not cliente:
            raise ValueError(f"No existe el cliente con id '{id_usuario}'")
        tarjeta = next(
            (t for t in self.tarjetas
             if t.numero == numero and t.codigo == codigo and t.id_usuario == id_usuario),
            None
        )
        if not tarjeta:
            return False
        self.tarjetas.remove(tarjeta)
        cliente.tarjetas.remove(tarjeta)
        self.guardar_tarjetas()
        return True