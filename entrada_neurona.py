from PIL import Image
from os import listdir
import os

def sacar_pixels(direccion, entrada):
    #se abre la imagen
    im = Image.open(direccion)
    im = im.resize((40, 10), Image.ANTIALIAS)
    #im.save("hola.jpg")
    #lectura de pixels
    pixels = im.load()
    #se abre el archivo para lectura escritura
    archivo_entrenamiento = open("datos-entrenamiento.csv", "a")
    filas, columnas = im.size
    decimales = 4
    for columna in range (columnas):
        for fila in range(filas):
            #se separan los valores RGB y se escriben en el archivo
            rojo = str(normalizar(pixels[fila,columna][0]))
            verde = str(normalizar(pixels[fila,columna][1]))
            azul = str(normalizar(pixels[fila,columna][2]))
            cadena = rojo[:rojo.find(".")+decimales] + " " + verde[:verde.find(".")+decimales] + " " + azul[:azul.find(".")+decimales] + " "
            archivo_entrenamiento.write(cadena)

    #pix[x,y] = value # Set the RGBA Value of the image (tuple) 
    archivo_entrenamiento.write(entrada)
    archivo_entrenamiento.write("\n")
    archivo_entrenamiento.close()

def recorrer_directorio(carpeta_entrada, lista_imagenes, salida):
    for nombre_imagen in lista_imagenes:
        print nombre_imagen
        sacar_pixels(carpeta_entrada + "/" +nombre_imagen, salida)

def normalizar(valor):
    salida = (valor*1.)/255.
    return salida
    

if(os.path.exists("datos-entrenamiento.csv")== True):
    os.remove("datos-entrenamiento.csv")
recorrer_directorio("tomates-recortados-buenos", listdir("./tomates-recortados-buenos"), "0 1 0")
recorrer_directorio("tomates-recortados-malos",  listdir("./tomates-recortados-malos"), "1 0 0")
recorrer_directorio("tomates-recortados-verdes", listdir("./tomates-recortados-verdes"), "0 0 1" )
