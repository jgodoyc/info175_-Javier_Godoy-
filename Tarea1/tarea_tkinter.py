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
	    	

def encriptacion():	
	encrypt()


ventana = Tk()
ventana.title("encriptacion")
ventana.geometry("400x500")

var = StringVar()
label = Label( ventana, text="Ingrese texto que desea encriptar")

texto_BOX = Text(ventana, height=15, width=55) #son caracteres de distancia
texto_BOX.place(x=5, y=20)	#son pixeles de distancia

opcion1 = Radiobutton(ventana, text="Cesar", value=1)
opcion1.place(x=10, y=255)
numSpin = Spinbox(ventana, from_=0, to=26, textvariable="numero")
numSpin.place(x=75, y=255)

opcion2 = Radiobutton(ventana, text="Cenit-Polar", value=2)
opcion2.place(x=200, y=255)

boton = Button(ventana, text="ENCRIPTAR", command=lambda:accionBoton())
boton.place(x=150, y=450)

#label2 = Label( ventana, textvariable= texto_BOX)
#label2.place(x=10, y=270)

textoEntr = texto_BOX.get("1.0",END)
label.pack()
#label2.pack()
#hasta aqui nomas quede no hacen nada los botones solo h
ventana.mainloop()
