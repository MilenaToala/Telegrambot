import datetime
import random as rd

class Vuelo:
    def __init__(self, destino, horas, fechas, origen):
        self.origen = origen
        self.destino = destino
        self.horas = horas
        self.fechas = fechas
        self.asientos = 180

    def __repr__(self):
        return "Aeropuerto destino: " + self.destino.__repr__() + ", fecha: " + self.fechas.isoformat() +", hora: " + self.horas.isoformat()


class Aeropuerto:
    def __init__(self, datos_json):
        self.nombre = datos_json["nombre"]
        self.iata = datos_json["iata"]
        self.pais = datos_json["pais"]
        self.estado = datos_json["provincia"]
        self.ciudad = datos_json["ciudad"]
        self.vuelos = []

    def generar_vuelos(self, aeropuertos, min_valor = 4, max_valor = 8):
        for i in range( 0, rd.randrange(min_valor, max_valor)):
            aeropuerto = self

            while aeropuerto == self:
                aeropuerto = aeropuertos[rd.randrange(0, len(aeropuertos))]

            hora = datetime.time(rd.randrange(0, 24), rd.randrange(0, 60))
            fecha = datetime.date.today() + datetime.timedelta(days= rd.randrange(1, 16))
            vuelo = Vuelo(aeropuerto, hora, fecha, self)
            self.vuelos.append(vuelo)

    def eliminar_vuelos(self):
        for vuelo in self.vuelos:
            print("Aeropuerto: " + vuelo.destino)

    def __repr__(self):
        return "Aeropuerto: " + self.nombre + ", país: " + self.pais
