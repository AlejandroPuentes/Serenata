# Serenata
Diagrama UML

## Integrantes:

- Brayan Alejandro Puentes Camargo  - 20181020044
- Johnatan Guillermo Ruiz Bautista  - 20181020034
- Juan Camilo Ramírez Rátiva        - 20181020089

### Diagrama UML

![alt text](https://github.com/wthoutjc/Serenata/blob/master/BandaUML.png)
### Principios Del Programa


#### **Principio Liskov**
<p align="justify">En este software puede observar claramente el liskov en la herencias de la clase instrumento ya que todas las clases derivadas también pueden ser tratadas como  la propia clase base, Esto significa que los objetos deben poder ser   
reemplazados por instancias de sus subtipos sin alterar el correcto funcionamiento del sistema o lo que es lo mismo. </p>

#### **Principio Responsabilidad Unica**
<p align="justify">Según este principio una clase debería tener una, y solo una, razón para cambiar. como podemos ver el programa deja a sus clases una y solo una tarea o respondabilidad, logrando así tener un bajo acoplamiento entre dichas clases.</p>  

#### **Principio Abierto-Cerrado**
<p align="justify">Como se puede observar este principio trata que las clases deben estar abiertos para las extensiones, pero cerrado para las modificaciones del código fuente. Este software cumple este pricipio ya que como podemos observar la clase "intrumentos" se instancia en la clase "Banda", pero esta no puede cambiar nada del funcionamiento de "instrumentos".Es decir, que el diseño del programa debe está abierto para poderse extender, pero cerrado para poder realizar modificaciones de su código fuente.</p>

