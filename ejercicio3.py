# -*- coding: utf-8 -*-

if __name__== "__main__":
	lista= []
	linea = ""
	existe = True
	while existe:
		print "Ingrese frase: "
		linea = raw_input()
		linea = linea.upper()
		if linea == "":
			existe = False
			break
		lista.append(linea)
	print lista
		

