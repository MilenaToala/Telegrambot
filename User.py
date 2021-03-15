from enum import Enum

class Estado(Enum):
    BUSCAR = 1
    COMPRAR_IDA = 2
    COMPRAR_LLEGADA = 3

class Registro:
    def __init__(self, vuelo, puestos):
        self.vuelo = vuelo
        self.puestos = puestos
        

class Usuario:
    def __init__(self, chat_id, stats= Estado.BUSCAR):
        self.chat_id = chat_id
        self.stats = stats
        self.vuelos_comprados = []
        self.Temp = []
        self.puestos_temp = 0

    def reset(self):
        self.Temp = []
        self.puestos_temp = 0
