from intento1 import Banda


banda = Banda()
banda.imprimir()
banda.construirBanda()
print("Que quiere hacer con la banda ")
print("1.Afine")
print("2.Empiece a tocar")
number=input()
if (number==1):
    print("LA BANDA EMPEZO A AFINAR")    
    banda.prepararSerenata()
else:
    print("LA BANDA EMPEZO A TOCAR")
    banda.tocarSerenata()


