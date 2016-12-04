
# coding: utf-8

# In[2]:

from pylab import *
from scipy.integrate import *
from binascii import *
from PIL import Image
from PIL import *
get_ipython().magic(u'matplotlib inline')


# In[6]:

def encode_image(img, msg):
    """
    usa la porcion roja de una imagen (r,g,b) para esconder el mensaje 
    en caracteres ascii y el valor rojo del primer pixel se utiliza como
    la longitud de la cadena
    """
    length = len(msg)
    # limite del mensaje=255 caracteres
    if length > 255:
        print("texto demasiado largo! ( max 255 caracteres)")
        return False
    if img.mode != 'RGB':
        print("La imagen debe estar en modo RGB")
        return False
    #copia la imagen para ocultar el mensaje
    encoded = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            # primer valos=longitud del mensaje
            if row == 0 and col == 0 and index < length:
                asc = length
            elif index <= length:
                c = msg[index -1]
                asc = ord(c)
            else:
                asc = r
            encoded.putpixel((col, row), (asc, g , b))
            index += 1
    return encoded
def decode_image(img):
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                
                r, g, b, a = img.getpixel((col, row))		
            # el valor del primer pixel r es la longitud del mensaje
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                msg += chr(r)
            index += 1
    return msg
original_file = "proof.png"

img = Image.open(original_file)
print(img, img.mode)  # test
encoded_image_file = "enc_" + original_file
secret_msg = "Mensaje oculto"
print(len(secret_msg))  # test
img_encoded = encode_image(img, secret_msg)
if img_encoded:
    img_encoded.save(encoded_image_file)
    print("{} saved!".format(encoded_image_file))
    import webbrowser
    webbrowser.open(encoded_image_file)


# In[7]:

#regresa el mensaje oculto
img2 = Image.open(encoded_image_file)
hidden_text = decode_image(img2)
print("Hidden text:\n{}".format(hidden_text))


# In[ ]:



