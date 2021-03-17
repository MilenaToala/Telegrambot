import datetime
import random as rnd

class Vuelo:
    def __init__(self, destino, horas, fechas, origen): #El método __init__ es un método especial de una clase en Python. El objetivo fundamental del método __init__ es inicializar los atributos del objeto que creamos.
        self.origen = origen
        self.destino = destino
        self.horas = horas
        self.fechas = fechas
        self.asientos = 180

    def __repr__(self): #el método __repr__ se usa para depuración y desarrollo, por lo que sus mensajes ha de ser inequívocos. Además, __repr__ calcula la representación de cadena “oficial” de un objeto
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
        for i in range( 0, rnd.randrange(min_valor, max_valor)):
            aeropuerto = self

            while aeropuerto == self:
                aeropuerto = aeropuertos[rnd.randrange(0, len(aeropuertos))]

            hora = datetime.time(rnd.randrange(0, 24), rnd.randrange(0, 60))
            fecha = datetime.date.today() + datetime.timedelta(days= rnd.randrange(1, 16))
            vuelo = Vuelo(aeropuerto, hora, fecha, self)
            self.vuelos.append(vuelo)

    def Borrar(self):
        for vuelo in self.vuelos:
            print("Aeropuerto: " + vuelo.destino)

    def __repr__(self):
        return "Aeropuerto: " + self.nombre + ", país: " + self.pais
