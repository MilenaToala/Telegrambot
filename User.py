from enum import Enum

class Estado(Enum):
    BUSCAR = 1
    COMPRAR_IDA = 2
    COMPRAR_LLEGADA = 3
    Volver = 4

class Usuario:
    def __init__(self, chat_id, stats= Estado.BUSCAR):
        self.chat_id = chat_id
        self.stats = stats
        self.vuelos_comprados = []
        self.Temp = []
        self.puestos_temp = 0

    def boot(self):
        self.Temp = []
        self.puestos_temp = 0
        


        

