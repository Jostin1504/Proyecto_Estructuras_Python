class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def solicitar_servicio(self, servicio):
        print(f"{self.nombre} ha solicitado el servicio de {servicio}.")

#en primera instancia con los clientes se usaria la cola
#el primero que se hace siempre queda de primero en el proceso de pago