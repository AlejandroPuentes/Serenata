from Instrumento import Instrumento

class Flauta (Instrumento):

    def __init__(self):
        self.preparandoImg = '/static/imagenes/pFlauta.png'
        self.tocandoImg = '/static/imagenes/tFlauta.png'

    def tocar(self):
        return"Tocando Flauta"
        
    def preparar(self):
        return'Preparando Flauta'