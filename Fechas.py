import csv
import uuid
from datetime import datetime, timedelta, timezone
class Tiempo:
    def __init__(self,fecha=None):
        self.fecha=datetime.now()
    def formato(self, formato="%Y-%m-%d %H:%M:%S"):
        return self.fecha.strftime(formato)
    def dias_diferencia(self,otra_fecha):
        if isinstance(otra_fecha,Tiempo):
            return(self.fecha-otra_fecha.fecha).days
        elif isinstance(otra_fecha,datetime):
            return (self.fecha-otra_fecha).days
        return None
    def sumatoria_dias(self,dias):
        return Tiempo(self.fecha+timedelta(days=dias))
@staticmethod
def Ahora():
    return Tiempo(datetime.now())
def parametros_Tiempo(self,nombre_="fecha"):
    return {nombre_:self.formatear()}
@staticmethod
def Setformato(fecha_str, formato="%Y-%m-%d %H:%M:%S"):
       return Tiempo(datetime.strptime(fecha_str, formato))
        