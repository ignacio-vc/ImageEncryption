#Librerias
#####################################

from PIL import Image
from sys import argv
import random

#####################################

#####################################
#A continuación se muestra el segmento de código que convierte 
#el mensaje introducido por el usuario a binario 
#y lo oculta en la imagen.
#####################################

def convertBin(caracter):
    bin = ''
    dec = ord(caracter)
    while dec > 0:
        bin = str(dec % 2) + bin
        dec >>= 1
    while len(bin) < 8:
        bin = '0' + bin
    return bin

def convertChar(bits):
    return chr(int(bits,2))

def ocultar(data):
    mensaje = input('Mensaje a Ocultar: ')
    rand = random.randrange(50)
    bloques = convertBin(str(len(mensaje)))

    bits = bloques
    for caracter in mensaje:
        bits += convertBin(caracter)
    
    (w,h) = data.size
    pixel = data.load()
    res = Image.new('RGB',(w,h))
    nuevo = res.load()

    i = 0
    for x in range(w):
        for y in range(h):
            r,g,b = pixel[x,y]
            if i < len(bits):
                if int(bits[i]) == 1:
                    if r % 2 == 1 and r < 255:
                        r += 1
                    elif r % 2 == 1 and r == 255:
                        r -= 1
                else:
                    if r % 2 == 0:
                        r += 1
            i += 1
            nuevo[x,y] = r,g,b
    res.save("imgsecret"+str(rand)+".png")
    print ('Mensaje Oculto')

#####################################
#Y ahora se muestran las funciones que recuperan un mensaje oculto en una imagen, 
#asi como los bloques de 8 bits que ocupa ese mensaje.
#####################################

def obtenerBloques(data):
    (w,h) = data.size
    pixel = data.load()
    bloqbin = ''
    for x in range(w):
        for y in range(h):
            r,g,b = pixel[x,y]
            if y < 8:
                if r % 2 == 0:
                    bloqbin += '0'
                else: 
                    bloqbin += '1'
            else:
                return int(bloqbin,2)

def recuperar(data):
    print ('Recuperando Mensaje...')
    (w,h) = data.size
    pixel = data.load()

    num = ''
    mensaje = ''
    bloques = obtenerBloques(data)+1

    c = 0
    for x in range(w):
        for y in range(h):
            r,g,b = pixel[x,y]
            if c < bloques:
                if r % 2 == 0:
                    num += '1'
                else:	
                    num += '0'
                if len(num) % 8 == 0:
                    if c != 0:
                        mensaje += convertChar(num[c*8:(c+1)*8])
                    c += 1
            else:
                return mensaje

def main():
    try:
        imagen = argv[2]
        if argv[1] == '-ocultar': #Oculta Informacion
            data = Image.open(imagen).convert('RGB')
            ocultar(data)
        elif argv[1] == '-recuperar': #Extrae Informacion
            new = Image.open(imagen).convert('RGB')
            mensaje = recuperar(new)
            print ('Mensaje Recuperado: ',mensaje)
    except:
        data = Image.open('ejemplo.png').convert('RGB')
        ocultar(data)
        new = Image.open('imgsecret.png').convert('RGB')
        mensaje = recuperar(new)
        print ('Mensaje Recuperado:',mensaje)


if __name__ == '__main__':
    main()

#####################################
#COMO EJECUTARLO:
#Para ocultar el mensaje escribir lo siguiente en la Terminal:
#$ python steganography.py -ocultar ejemplo.png 
#Para recuperar el mensaje escribir lo siguiente en la Terminal:
#$ python steganography.py -recuperar imgsecretn.png
#n es el numero de imagene que se genero con el mensaje oculto
#####################################






