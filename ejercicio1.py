# -*- coding: utf-8 -*-


def compara(x, y):
	if (x>y):
		print x," es mayor que ",y
	elif(x<y):
		print y, "es mayor que ",x
	else:
		print "los numeros sin iguales."

if __name__ == "__main__":
	x= input("ingrese un numero entero ")
	y= input("ingrese otro numero entero ")
	
	compara(x, y)
