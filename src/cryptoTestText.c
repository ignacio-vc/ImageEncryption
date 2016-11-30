/*Chicos, estoy probando unos algoritmos para familiarizarme con esto, 
y cómo lo que hablo más fluido es C...pos :P prometo traducir a py...
Nacho, resulta que 
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define LIMITE 500

char* cifrado_cesar(char mensaje[], int llave){
	
	char cifrado[LIMITE];

	for (int i = 0; i < strlen(mensaje); ++i)
	{
		cifrado[i] = (mensaje[i] + llave) % 27;
	}

	return (cifrado);
}

int main()
{
	char mensajeOrig[LIMITE],*mensajeCif[LIMITE];
	int key;

	printf("El siguiente programa cifra y decifra un texto de hasta 500 caracteres. \n");
	
	printf("Por favor ingresa el mensaje y cuando se te solicite ingresa también una llave\n");
	scanf("%s",mensajeOrig);

	printf("Ingresa una llave entre 0 y 26\n");
	scanf("%d",key);
	return 0;
}