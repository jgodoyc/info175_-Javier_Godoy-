from Tkinter import *
import string

def cenit_polar(frase):
	transformado = ""
	for t in frase:
		if t=="C" or t=="c" or t=="E" or t=="e" or t=="N" or t=="n" or t=="I" or t=="i" or t=="T" or t=="t":
			t = cenit(t)

		elif t=="P" or t=="p" or t=="O" or t=="o" or t=="L" or t=="l" or t=="A" or t=="a" or t=="R" or t=="r":
			t = polar(t)

		transformado += t
	return transformado

def cenit(car):
	car = car.replace("C", "P")
	car = car.replace("c", "p")
	car = car.replace("E", "O")
	car = car.replace("e", "o")
	car = car.replace("N", "L")
	car = car.replace("n", "l")
	car = car.replace("I", "A")
	car = car.replace("i", "a")
	car = car.replace("T", "R")
	car = car.replace("t", "r")
	return car

def polar(car):
	car = car.replace("P", "C")
	car = car.replace("p", "c")
	car = car.replace("O", "E")
	car = car.replace("o", "e")
	car = car.replace("L", "N")
	car = car.replace("l", "n")
	car = car.replace("A", "I")
	car = car.replace("a", "i")
	car = car.replace("R", "T")
	car = car.replace("r", "t")
	return car


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
	    	

def escriptacion:	
	encrypt()


	