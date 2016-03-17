# -*- coding: utf-8 -*-

if __name__== "__main__":
	lista= []
	linea = ""
	existe = True
	while existe:
		print "Ingrese frase: "
		linea = raw_input()
		if linea == "":
			existe = False
		lista.append(linea)
	
		

