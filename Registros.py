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
        return "Lugar de llegada: " + self.destino.mostrar() + ","+" fecha de llegada: " + self.fecha.isoformat() +","+" hora de llegada: " + self.hora.isoformat()

#usamos un archivo.json para acceder a los datos
class Aeropuertos:
    def registrar(self, data):
        self.nombre = data["nombre"]
        self.iata = data["iata"]
        self.pais = data["pais"]
        self.estado = data["provincia"]
        self.ciudad = data["ciudad"]
        self.registros = []

    def nuevo_vuelo(self, ap1, min_Registros = 4, max_Registros = 8):
        for i in range( 0, rnd.randrange(min_Registros, max_Registros)):
            aport = self

            while aport == self:
                aport = ap1[rnd.randrange(0, len(ap1))]

            hora = datetime.time(rnd.randrange(0, 24), rnd.randrange(0, 60))
            fecha = datetime.date.today() + datetime.timedelta(days= rnd.randrange(1, 16))
            fly = vuelos(ap, hora, fecha, self)
            self.registros.append(fly)

    def borrar(self):
        for fly in self.registros:
            print("Destino: " + fly.destino)

    def mostrar(self):
        return "Destino: " + self.nombre + ", país: " + self.pais
