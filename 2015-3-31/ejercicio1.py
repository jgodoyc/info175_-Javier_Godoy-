class auto():
	def __init__(self, bencina, encendido, kilometraje, rendimiento):
		self.bencina = bencina
		self.encendido = encendido
		self.kilometraje = kilometraje
		self.rendimiento = rendimiento
	

	def encender(self):
		if self.encendido == False:
			self.encendido = True
			print("esta encendido el auto")

	def apagar(self):
		if self.encendido == True:
			self.encendido = False
			print("se a apagado el auto")

	def Mover(self, kil):
		self.encender()
		bencinaUsada = kil / self.rendimiento
		if self.bencina >= bencinaUsada:
			print("Se ha avanzado "+ str(kil) +" kilometros")
			self.bencina -= bencinaUsada
			self.kilometraje += kil
		else:
			print("No alcanzara a llegar a su destino.")
			self.encendido= False
			print("Se a apagado el auto")			

	def Obtener_kilometraje(self):
		print("EL kilometraje del auto es :"+ str(self.kilometraje))

	def Obtener_bencina(self):
		print("La bencina que hay es: " + str(self.bencina))

	def Cargar_bencina(self, lts):
		self.apagar()
		if lts > 0:
			self.bencina += lts
			print("Bencina total es: " + str(self.bencina))

mi_autito = auto(10,False,0,13)
mi_autito.Obtener_bencina()
mi_autito.Obtener_kilometraje()
ben = input("Cuantos litros de vencina va a cargar?\n ")
mi_autito.Cargar_bencina(ben)
kil = input("De cuantos kilometros sera su viaje? \n")		
mi_autito.Mover(kil)


