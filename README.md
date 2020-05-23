# Serenata


## Integrantes:

- Brayan Alejandro Puentes Camargo  - 20181020044
- Johnatan Guillermo Ruiz Bautista  - 20181020034
- Juan Camilo Ramírez Rátiva        - 20181020089

### Diagrama UML

![alt text](https://github.com/wthoutjc/Serenata/blob/master/BandaUML2.0.png)
### Descripcion Del Programa
<p align= "Justify">Este programa simula la preparación de una orquesta que cuenta con un número aleatorio de músicos a los cuales les corresponden un instrumento, estos instrumentos pueden ser de cinco tipos diferentes (trompeta, guitarra, flauta, violín, batería) los cuales serán asignados aleatoriamente a los diferentes músicos que tendrán la dos funciones: alistarse y tocar la banda.</p>

### Requisitos
<p align= "Justify">Este programa fue diseñado en Python 3.7.3, para poder correr este programa se necesita tener las librerías random y flask.</p>

### Principios De Diseño


#### **Principio Liskov**
<p align="justify">En este software puede observar claramente el liskov en la herencias de la clase instrumento ya que todas las clases derivadas también pueden ser tratadas como  la propia clase base, Esto significa que los objetos deben poder ser   
reemplazados por instancias de sus subtipos sin alterar el correcto funcionamiento del sistema o lo que es lo mismo. </p>

#### **Principio Responsabilidad Unica**
<p align="justify">Según este principio una clase debería tener una, y solo una, razón para cambiar. como podemos ver el programa deja a sus clases una y solo una tarea o respondabilidad, logrando así tener un bajo acoplamiento entre dichas clases.</p>  

#### **Principio Abierto-Cerrado**
<p align="justify">Como se puede observar este principio trata que las clases deben estar abiertos para las extensiones, pero cerrado para las modificaciones del código fuente. Este software cumple este pricipio ya que como podemos observar la clase "intrumentos" se instancia en la clase "Banda", pero esta no puede cambiar nada del funcionamiento de "instrumentos".Es decir, que el diseño del programa debe está abierto para poderse extender, pero cerrado para poder realizar modificaciones de su código fuente.</p>

### Patrones de Diseño

#### **Patron Abstract Factory**
<p align= "Justify">El patrón creacional abstract factory fue implementado en el código con el objetivo de poder abstraer la forma como se crean los objetos que representan los instrumentos, y para ello se implementa una interfaz para crear los métodos de preparar y tocar banda.</p>


