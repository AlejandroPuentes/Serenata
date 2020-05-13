import random
from Violin import Violin
from Acordeon import Acordeon
from Flauta import Flauta
from Bajo import Bajo
from Guitarra import Guitarra

class Banda:
    def __init__(self):
        self.cantidad1 = random.randint(5,10)
        self.instrumentos = []

    def imprimir(self):
        print(self.cantidad1)

    def generarInstrumento(self):
        for i in range(self.cantidad1):
            self.tipoins = random.randrange(5)
            print('Tipo ins -> ' + str(self.tipoins))
            if self.tipoins == 0:
                violin = Violin()
                return violin
            elif self.tipoins == 1:
                guitarra = Guitarra()
                return guitarra
            elif self.tipoins == 2:
                acordeon = Acordeon()
                return acordeon
            elif self.tipoins == 3:
                flauta = Flauta()
                return flauta
            else:
                bajo = Bajo()
                return bajo
    
    def construirBanda(self):
        selec = Banda()
        for i in range(self.cantidad1):
            self.instrumentos.append(selec.generarInstrumento())
        print(self.instrumentos)

    def tocarSerenata(self):
        for i in range(self.cantidad1):
            self.instrumentos[i].tocar()
    
    def prepararSerenata(self):
        for i in range(self.cantidad1):
            self.instrumentos[i].preparar()













