from PIL import Image
from os import listdir

def sacar_pixels(direccion):
    #se abre la imagen
    im = Image.open(direccion) 
    #lectura de pixels
    pixels = im.load()
    #se abre el archivo para lectura escritura
    archivo_entrenamiento = open("datos-entrenamiento.csv", "a")
    filas, columnas = im.size
    for columna in range (columnas):
        for fila in range(filas):
            #se separan los valores RGB y se escriben en el archivo
            cadena = str(pixels[fila,columna][0]) + " " + str(pixels[fila,columna][1]) + " " + str(pixels[fila,columna][2]) + " "
            archivo_entrenamiento.write(cadena)

    #pix[x,y] = value # Set the RGBA Value of the image (tuple) 
    archivo_entrenamiento.write("\n")
    archivo_entrenamiento.close()

def recorrer_directorio(carpeta_entrada, lista_imagenes, salida_esperada):
    for nombre_imagen in lista_imagenes:
        sacar_pixels(carpeta_entrada + "/" +nombre_imagen, salida_esperada)

recorrer_directorio("tomates-recortados-buenos", listdir("./tomates-recortados-buenos"))
recorrer_directorio("tomates-recortados-malos",  listdir("./tomates-recortados-malos"))