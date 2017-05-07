from PIL import Image
from os import listdir

def sacar_pixels(direccion, archivo):
    #se abre la imagen
    im = Image.open(direccion)
    im = im.resize((50, 10), Image.ANTIALIAS)
    #im.save("hola.jpg")
    #lectura de pixels
    pixels = im.load()
    #se abre el archivo para lectura escritura
    archivo_entrenamiento = open(archivo, "a")
    filas, columnas = im.size
    for columna in range (columnas):
        for fila in range(filas):
            #se separan los valores RGB y se escriben en el archivo
            cadena = str(normalizar(pixels[fila,columna][0])) + " " + str(normalizar(pixels[fila,columna][1])) + " " + str(normalizar(pixels[fila,columna][2])) + " "
            archivo_entrenamiento.write(cadena)

    #pix[x,y] = value # Set the RGBA Value of the image (tuple) 
    archivo_entrenamiento.write("\n")
    archivo_entrenamiento.close()

def recorrer_directorio(carpeta_entrada, lista_imagenes, archivo):
    for nombre_imagen in lista_imagenes:
        sacar_pixels(carpeta_entrada + "/" +nombre_imagen, archivo)

def normalizar(valor):
    return 0
    

recorrer_directorio("tomates-recortados-buenos", listdir("./tomates-recortados-buenos"), "tomates-recortados-buenos.csv")
recorrer_directorio("tomates-recortados-malos",  listdir("./tomates-recortados-malos"), "tomates-recortados-malos.csv")
recorrer_directorio("tomates-recortados-verdes-buenos", listdir("./tomates-recortados-verdes-buenos"), "tomates-recortados-verdes-buenos.csv")