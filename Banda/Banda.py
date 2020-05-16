import random
from Violin import Violin
from Bateria import Bateria
from Flauta import Flauta
from Trompeta import Trompeta
from Guitarra import Guitarra


class Banda:
    def __init__(self):
        self.instrumentos = []

    def getInstrumentos(self):
        return self.instrumentos

    def getCantidad(self):
        return len(self.instrumentos)

    def generarInstrumento(self):
        tipoins = random.randrange(5)
        if tipoins == 0:
            return Violin()
        elif tipoins == 1:
            return Guitarra()
        elif tipoins == 2:
            return Bateria()
        elif tipoins == 3:
            return Flauta()
        else:
            return Trompeta()

    def construirBanda(self):
        self.instrumentos = []
        for i in range(random.randrange(5, 11)):
            self.instrumentos.append(self.generarInstrumento())

    def tocarSerenata(self):
        for instrumento in self.instrumentos:
            instrumento.tocar()

    def prepararSerenata(self):
        for instrumento in self.instrumentos:
            instrumento.preparar()

