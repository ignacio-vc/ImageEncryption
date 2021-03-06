# ImageEncryption

Proyecto para Fisica Computacional 2017-1 con Rich

#### Autores:
- [Adriana Rosalia Sanchez Montes](https://github.com/adriross "adriross")
- [Ismael Velázquez Gómez](https://github.com/iselplabo93 "iselplabo93")
- [Raúl Ramírez](https://github.com/jatib "jatib")
- [Ignacio Vargas Cordero](https://github.com/ignacio-vc "ignacio-vc")

#### Estructura de Directorios:
- docs: Documentacion y Presentacion
- src: Archivos .py, esta bien hacer merge de estos
- test: Tests
- wip: Work in Progress, Jupyter Notebooks y demas

#### Comandos para commits

```
git status
git add TuArchivoAqui
#git checkout -- ElArchivoDelOtroAqui
git commit -m "MiCommitAqui"
git pull
#git mergetool -t meld (si hay problemas)
#git commit -m ¨MiMergeAqui¨
git push
```

#### Referencias:

##### Métodos de Encriptación

[Cifrado y Descifrado de Imágenes](https://github.com/PabloJC/Cifrado-y-Descifrado-de-Imagenes/blob/master/Criptosistema.py)

[Cifrado Vigenere](https://d14m4nt3.wordpress.com/2012/07/31/cifrado-vigenere-y-algo-de-python/)

[Sistema de Encriptación](https://codigosolucion.wordpress.com/2014/10/19/crear-un-sistema-de-encriptacion-en-python/)

[Cifrado XOR](http://www.adrastea.es/blog/tag/python/)

[2D Logistic-adjusted-sine map](http://www.sciencedirect.com/science/article/pii/S0020025516000281)

[Secret Sharing Schemes](http://ruxandraolimid.weebly.com/uploads/2/0/1/0/20109229/jisom_2013_paper.pdf)

[Caesar Cipher](http://inventwithpython.com/chapter14.html)

[Cryptopals Challenges](http://cryptopals.com/)

[Chaos based cryptosystem using external key](http://scipy.in/2012/static/slides/cryptosystem.pdf)

[Cryptography with Chaos](http://www.cmsim.org/images/1_CHAOS2012_Proceedings_Papers_M-P.pdf)

[A Brief Notebook on Cryptography](http://davidlowryduda.com/a-brief-notebook-on-cryptography/)

##### Steganography

[Examples](https://github.com/lopezezequiel/steganosaurus-py/blob/master/example.py)

[Steganography with Images](http://hackliza.blogspot.mx/2012/10/outra-de-esteganografia-con-imaxes.html)

[Message to Binary](https://gist.github.com/soul0592/5955341)

[Hiding in plain sight](http://interactivepython.org/runestone/static/everyday/2012/03/1_steganography.html)

[Open Source Data Security](http://clubhack.com/2009/files/Suhas_Desai__Open_Source_Data_Security.pdf)

##### Cellular Automata (Imagenes)

[Chaotic Encryption Method Based on Life-like Cellular Automata](http://arxiv.org/pdf/1112.6326v1.pdf "articulo")

[The Research of Image Encryption Algorithms Based on Chaos Cellular Automata](https://pdfs.semanticscholar.org/bff7/e1fc9a4201e9b50b16314ceffd13c024edf4.pdf "articulo")

[New Possiblities for Cellular Automata in Cryptography](http://www.criptored.upm.es/cibsi/cibsi2011/info/Ponencias/5.%20New%20Possibilities%20for%20Cellular%20Automata%20in%20Cryptography.pdf "presentacion")

#### Configurar word wraping en Jupyter.

- Primero, buscamos el directorio de configuración de Jupyter
	```
	jupyter --config-dir
	```
- En mi caso es 
	```
	~/.jupyter
	```
- Editar, o crear:
	```
	nbconfig/notebook.json
	```
- Y agregar:

	```
	{
	  "MarkdownCell": {
	    "cm_config": {
	      "lineWrapping": true
	    }
	  },
	  "CodeCell": {
	    "cm_config": {
	      "lineWrapping": true
	    }
	  }
	}
	```
	
- Por último reiniciar Jupyter-Notebook
