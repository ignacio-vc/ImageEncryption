#ImageEncryption

#math: funciones matematicas
import math
#os: da habilidad de usar funciones dependientes en el sistema operativo 
import os
#PyCrypto: nos da funciones de hash seguras y algoritmos de encripcion
from Crypto.Cipher import AES
#hashlib: implementa una interface comun a varios algoritmos de hash seguros
import hashlib
#binascii: contiene metodos para convertir entre binario y representarios de binario codificadas con ASCII
import binascii
#Tkinter: paquete GUI default
from Tkinter import *
from tkFileDialog import *
import tkMessageBox
#PIL: Python Image Library, agrega la capacidad de manipular imagenes
from PIL import Image

global password # declare global variable "password"

#ENCRYPTION METHOD:

def encrypt(imagename, password):
    # we initialize variables
    plaintext = list()
    plaintextstr = ""

    # load the desired image
    im = Image.open(imagename)
    pix = im.load()

    #print im.size   # print size of image (width,height)
    width = im.size[0]
    height = im.size[1]

    # break up the image into a list, each with pixel values and then append to a string
    for y in range(0,height):
        #print("Row: %d") %y  # print row number
        for x in range(0,width):
            #print pix[x,y]  # print each pixel RGB tuple
            plaintext.append(pix[x,y])

    # add 100 to each tuple value to make sure each are 3 digits long.  being able to do this is really just a PoC
    # that you'll be able to use a raw application of RSA to encrypt, rather than PyCrypto if you wanted.
    for i in range(0,len(plaintext)):
        for j in range(0,3):
            plaintextstr = plaintextstr + "%d" %(int(plaintext[i][j])+100)

    # length save for encrypted image reconstruction
    relength = len(plaintext)

    # append dimensions of image for reconstruction after decryption
    plaintextstr += "h" + str(height) + "h" + "w" + str(width) + "w"

    # make sure that plantextstr length is a multiple of 16 for AES.  if not, append "n".  not safe in theory
    # and i should probably replace this with an initialization vector IV = 16 * '\x00' at some point.  In practice
    # this IV buffer should be random.
    while (len(plaintextstr) % 16 != 0):
        plaintextstr = plaintextstr + "n"

    # encrypt plaintext
    obj = AES.new(password, AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(plaintextstr)

    # write ciphertext to file for analysis
    cipher_name = imagename + ".crypt"
    g = open(cipher_name, 'w')
    g.write(ciphertext)

    # -----------------
    # construct encrypted image (not currently using since Tkinter isn't very nice)
    # -----------------
    def construct_enc_image():
        # hexlify the ciphertext
        asciicipher = binascii.hexlify(ciphertext)

        # replace function
        def replace_all(text, dic):
            for i, j in dic.iteritems():
                text = text.replace(i, j)
            return text

        # use replace function to replace ascii cipher characters with numbers
        reps = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25', 'z':'26'}
        asciiciphertxt = replace_all(asciicipher, reps)

        # construct encrypted image
        step = 3
        encimageone=[asciiciphertxt[i:i+step] for i in range(0, len(asciiciphertxt), step)]
        # if the last pixel RGB value is less than 3-digits, add a digit a 1
        if int(encimageone[len(encimageone)-1]) < 100:
            encimageone[len(encimageone)-1] += "1"
        # check to see if we can divide the string into partitions of 3 digits.  if not, fill in with some garbage RGB values
        if len(encimageone) % 3 != 0:
            while (len(encimageone) % 3 != 0):
                encimageone.append("101")

        encimagetwo=[(int(encimageone[int(i)]),int(encimageone[int(i+1)]),int(encimageone[int(i+2)])) for i in range(0, len(encimageone), step)]

        # make sizes of images equal
        while (int(relength) != len(encimagetwo)):
            encimagetwo.pop()

        # encrypted image
        encim = Image.new("RGB", (int(width),int(height)))
        encim.putdata(encimagetwo)

        encim.show()
        # alert success and path to image
        enc_success(cipher_name)

    construct_enc_image()
    
# decryption method
# -----------------
def decrypt(ciphername,password):

    # reach ciphertext into memory
    cipher = open(ciphername,'r')
    ciphertext = cipher.read()

    # decrypt ciphertext with password
    obj2 = AES.new(password, AES.MODE_CBC, 'This is an IV456')
    decrypted = obj2.decrypt(ciphertext)

    # parse the decrypted text back into integer string
    decrypted = decrypted.replace("n","")

    # extract dimensions of images
    newwidth = decrypted.split("w")[1]
    newheight = decrypted.split("h")[1]

    # replace height and width with emptyspace in decrypted plaintext
    heightr = "h" + str(newheight) + "h"
    widthr = "w" + str(newwidth) + "w"
    decrypted = decrypted.replace(heightr,"")
    decrypted = decrypted.replace(widthr,"")

    # reconstruct the list of RGB tuples from the decrypted plaintext
    step = 3
    finaltextone=[decrypted[i:i+step] for i in range(0, len(decrypted), step)]
    finaltexttwo=[(int(finaltextone[int(i)])-100,int(finaltextone[int(i+1)])-100,int(finaltextone[int(i+2)])-100) for i in range(0, len(finaltextone), step)]

    # reconstruct image from list of pixel RGB tuples
    newim = Image.new("RGB", (int(newwidth), int(newheight)))
    newim.putdata(finaltexttwo)
    newim.show()

# ---------------------
# GUI stuff starts here
# ---------------------

# empty password alert
def pass_alert():
   tkMessageBox.showinfo("Password Alert","Please enter a password.")

def enc_success(imagename):
   tkMessageBox.showinfo("Success","Encrypted Image: " + imagename)

# image encrypt button event
def image_open():
    # useless for now, may need later
    global file_path_e

    # check to see if password entry is null.  if yes, alert
    enc_pass = passg.get()
    if enc_pass == "":
        pass_alert()
    else:
        password = hashlib.sha256(enc_pass).digest()
        filename = askopenfilename()
        file_path_e = os.path.dirname(filename)
        # encrypt the image
        encrypt(filename,password)

# image decrypt button event
def cipher_open():
    # useless for now, may need later
    global file_path_d

    # check to see if password entry is null.  if yes, alert
    dec_pass = passg.get()
    if dec_pass == "":
        pass_alert()
    else:
        password = hashlib.sha256(dec_pass).digest()
        filename = askopenfilename()
        file_path_d = os.path.dirname(filename)
        # decrypt the ciphertext
        decrypt(filename,password)

# main gui app starts here
class App:
  def __init__(self, master):
    # make passg global to use in functions
    global passg
    # setup frontend titles etc blah blah
    title = "Image Encryption"
    msgtitle = Message(master, text =title)
    msgtitle.config(font=('helvetica', 17, 'bold'), width=200)
    
    # draw canvas
    canvas_width = 200
    canvas_height = 50
    w = Canvas(master,
           width=canvas_width,
           height=canvas_height)

    # pack the GUI, this is basic, we shold use a grid system
    msgtitle.pack()
    w.pack()

    # password field here above buttons
    passlabel = Label(master, text="Enter Encrypt/Decrypt Password:")
    passlabel.pack()
    passg = Entry(master, show="*", width=20)
    passg.pack()

    # add both encrypt/decrypt buttons here which trigger file browsers
    self.encrypt = Button(master,
                         text="Encrypt", fg="black",
                         command=image_open, width=25,height=5)
    self.encrypt.pack(side=LEFT)
    self.decrypt = Button(master,
                         text="Decrypt", fg="black",
                         command=cipher_open, width=25,height=5)
    self.decrypt.pack(side=RIGHT)

root = Tk()
root.wm_title("Image Encryption")
app = App(root)
root.mainloop()