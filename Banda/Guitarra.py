from Instrumento import Instrumento

class Guitarra(Instrumento):

    def __init__(self):
        self.preparandoImg = '/static/imagenes/pGuitarra.png'
        self.tocandoImg = '/static/imagenes/tGuitarra.png'

    def tocar(self):
        return "Tocando Guitarra" 

    def preparar(self):
        return'Afinando Guitarra'
    