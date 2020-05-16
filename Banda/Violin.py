from Instrumento import Instrumento

class Violin (Instrumento):

    def __init__(self):
        self.preparandoImg = '/static/imagenes/pViolin.png'
        self.tocandoImg = '/static/imagenes/tViolin.png'

    def tocar(self):
        return "Tocando Violin"

    def preparar(self):
        return 'Afinando Violin' 