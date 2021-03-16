import datetime
import random as rnd
import calendar
import pprint

class vuelos:
    def registrar(self, fecha, hora, destino, origen):
        self.fecha = fecha
        self.hora = hora
        self.origen = origen
        self.destino = destino
        self.asientos = 180

    def mostrar(self):
        return "Lugar de llegada: " + self.destino.mostrar() + ", fecha de llegada: " + self.fecha.isoformat() +", hora de llegada: " + self.hora.isoformat()


class Aeropuertos:
    def registrar(self, datos_json):
        self.nombre = datos_json["nombre"]
        self.iata = datos_json["iata"]
        self.pais = datos_json["pais"]
        self.estado = datos_json["provincia"]
        self.ciudad = datos_json["ciudad"]
        self.region = datos_json["region"]
        self.Registros = []

    def nuevo_vuelo(self, ap, min_Registros = 4, max_Registros = 8):
        for i in range( 0, rnd.randrange(min_Registros, max_Registros)):
            aport = self

            while ap == self:
                ap = ap[rnd.randrange(0, len(aport))]

            hora = datetime.time(rnd.randrange(0, 24), rnd.randrange(0, 60))
            fecha = datetime.date.today() + datetime.timedelta(days= rnd.randrange(1, 16))
            fly = Vuelo(ap, hora, fecha, self)
            self.Registros.append(fly)

    def borrar(self):
        for fly in self.Registros:
            print("Destino: " + fly.destino)

    def mostrar(self):
        return "Destino: " + self.nombre + ", país: " + self.pais
