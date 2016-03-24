import string
def encrypt(palabra, N):
	abcdario=string.ascii_lowercase
	palabraRara = ""
	for caracter in palabra:
		j=0
    	for letra in abcdario:
    		if caracter == letra:
    			palabraRara += abcdario[j+N]
    		else:
    			j = j+ 1
    print (palabraRara)

if __name__ == "__main__":
	palabra = raw_input("Escriba una palabra: ")
	N = input("Ingrese un entero: ")
	bla = encrypt(palabra, int(N))
	print (bla)