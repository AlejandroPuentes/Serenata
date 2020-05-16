from Instrumento import Instrumento

class Trompeta (Instrumento):

    def __init__(self):
        self.preparandoImg = '/static/imagenes/pTrompeta.png'
        self.tocandoImg = '/static/imagenes/tTrompeta.png'

    def tocar(self):
        return "Tocando Trompeta"

    def preparar(self):
        return 'Preparando Trompeta'