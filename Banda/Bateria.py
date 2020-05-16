from Instrumento import Instrumento



class Bateria (Instrumento):

    def __init__(self):
        self.preparandoImg = '/static/imagenes/pBateria.png'
        self.tocandoImg = '/static/imagenes/tBateria.png'

    def tocar(self):
        return"Tocando Batería"
        
    def preparar(self):
        return'Preparando Batería'