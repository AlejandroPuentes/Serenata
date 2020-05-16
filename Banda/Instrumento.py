class Instrumento:

    def __init__(self):
        self.preparandoImg = ''
        self.tocandoImg = ''

    def tocar(self):
        pass
    
    def preparar(self):
        pass

    def getTocarImg(self):
        return self.tocandoImg

    def getPrepararImg(self):
        return self.preparandoImg
