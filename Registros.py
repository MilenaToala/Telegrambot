import datetime
import random as rd

class Recorrido:
    def registrar(self, destino, hora, fecha, origen):
        self.aero_1 = origen
        self.aero_2 = destino
        self.hora = hora
        self.fecha = fecha
        self.asientos = 180

    def mostrar(self):
        return "Lugar de LLegada: " + self.aero_2.mostrar() + ", fecha de llegada: " + self.fecha.isoformat() +", hora de llegada: " + self.hora.isoformat()


class Aeropuerto:
    def comienzo(self, data):
        self.nombre = data["nombre"]
        self.iata = data["iata"]
        self.pais = data["pais"]
        self.estado = data["provincia"]
        self.ciudad = data["region"]
        self.fly = []

    def nuevos_vuelos(self, aeroptos, min_valor = 4, max_valor = 8):
        for i in range( 0, rd.randrange(min_valor, max_valor)):
            aeropuerto_12 = self

            while aeropuerto_12 == self:
                aeropuerto_12 = aeroptos[rd.randrange(0, len(aeroptos))]

            hora = datetime.time(rd.randrange(0, 24), rd.randrange(0, 60))
            fecha = datetime.date.today() + datetime.timedelta(days= rd.randrange(1, 16))
            avion = Recorrido(aeropuerto_12, hora, fecha, self)
            self.fly.append(avion)

    def borrar(self):
        for avion in self.fly:
            print("Aeropuerto: " + avion.aero_2)

    def mostrar(self):
        return "Aeropuerto: " + self.nombre + ", país: " + self.pais
