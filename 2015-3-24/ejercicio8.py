# -*- coding: utf-8 -*-

import string

def encrypt():
	palabra = raw_input("Escriba una palabra: ")
	N = input("Ingrese un entero: ")

	abcdario = string.ascii_lowercase
	palabraRara = ""
	for caracter in palabra:
		for j in range (0,len(palabra)):
			if caracter == abcdario[j]:
				palabraRara += abcdario[j + N]    		
	print (palabraRara)
	    	

if __name__ == "__main__":	
	encrypt()
	