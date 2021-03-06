import datetime
import random as rnd

class Recorrido:
    def __init__(self, destino, horas, fechas, origen): #El método __init__ es un método especial de una clase en Python. El objetivo fundamental del método __init__ es inicializar los atributos del objeto que creamos.
        self.origen = origen
        self.destino = destino
        self.horas = horas
        self.fechas = fechas
        self.asientos = 180

    def __repr__(self): #el método __repr__ se usa para depuración y desarrollo, por lo que sus mensajes ha de ser inequívocos. Además, __repr__ calcula la representación de cadena “oficial” de un objeto
        return "Aeropuerto destino: " + self.destino.__repr__() + ", fecha: " + self.fechas.isoformat() +", hora: " + self.horas.isoformat()


class Aport:
    def __init__(self, data):
        self.iata = data["iata"]
        self.nombre = data["nombre"]
        self.pais = data["pais"]
        self.estado = data["provincia"]
        self.ciudad = data["ciudad"]
        self.region = data["region"]
        self.arrayv1 = []

    def new_vuelo(self, aptos, min_valor = 4, max_valor = 8):
        for i in range( 0, rnd.randrange(min_valor, max_valor)):
            aeropuerto = self

            while aeropuerto == self:
                aeropuerto = aptos[rnd.randrange(0, len(aptos))]

            hora = datetime.time(rnd.randrange(0, 24), rnd.randrange(0, 60))
            fecha = datetime.date.today() + datetime.timedelta(days= rnd.randrange(1, 16))
            vuelo = Recorrido(aeropuerto, hora, fecha, self)
            self.arrayv1.append(vuelo)

    def Borrar(self):
        for vuelo in self.arrayv1:
            print("Aeropuerto: " + vuelo.destino)

    def __repr__(self):
        return "Aeropuerto: " + self.nombre + ", país: " + self.pais
