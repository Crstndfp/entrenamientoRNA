# Madurez de tomates usando un RNA
Este conjunto de programas tiene como objetivo poder dar una probabilidad de madurez de los tomates, tiene dos objetivos a cumplir:
-	Entrenar una red neuronal artificial con el fin de poder detectar la madurez de los tomates.
-	Tener una aplicación de escritorio por el cual un usuario pueda analizar un tomate cualquiera.

# Características!

-	Cuenta con su propia RNA, pero puede entrenar la propia.
-	Solo se necesita tener clasificadas las imágenes en verde, maduro y podrido para poder entrenar la neurona.
-	Una interfaz gráfica para analizar la madurez de un tomate. 

> La idea principal es que solo se necesite
> de tomates para reconocer tomates.

## Tecnología 
Este proyecto utiliza una serie de proyectos de código abierto para funcionar correctamente:
* [OpenCV](http://opencv.org/) – Biblioteca para el tratado de imágenes.
* [Neurolab](https://pythonhosted.org/neurolab/) -  biblioteca de redes neuronales algoritmos básicos con configuraciones de red flexibles y algoritmos de aprendizaje.
* [Tkinter](https://wiki.python.org/moin/TkInter) Interfaz gráfica para Python 


Y por supuesto este proyecto es de código abierto con un repositorio público
En GitHub.

## Installation

Se necesita de [Python](https://www.python.org/) 2.7 para correr los programas.

Instalar las bibliotecas necesarias para el entrenamiento de la RNA: 

```sh
$ pip install opencv-python
$ pip install neurolab
```

### Instrucciones de uso
La descripción del proyecto y de las instrucciones del uso de las bibliotecas para usarlas en otros proyectos está en.

| LUGAR | INSTRUCCIONES |
| ------ | ------ |
| OneDrive | drive.google.com/open?id=1ooOKdeYSye6z-qe_OriWBdd-nlLm_1G7QtBQcbGXvKM

### Entrenar la RNA
Para entrenar su propia RNA.
- Clasifique todas las imágenes de tomates a las que tenga acceso, entre, verde, maduro y podrido, cree las siguientes capertas y coloquelos ahi>
    - tomates-verdes:   tomates verdes
    - tomates-buenos:   tomates maduros
    - tomates-malos:    tomates podridos
- cree las siguientes carpetas, ahi se almacenaran recortes de los tomates.
    - tomates-recortados-buenos
    - tomates-recortados-malos
    - tomates-recortados-verdes

- Ejecute los siguientes comandos, tome en cuenta que el entrenamiento es tardado y depende de la capacidad de computo y cantidad de imagenes que se utilizen para entrenar.
    ```sh
    $ python recortar_tomates.py
    $ python entrada_neurona.py
    $ python Red_neuronal.py
    ```
### Reconocer un tomate
```sh
$ cd grafico
$ python interfaz.py
```
License
----
GPL