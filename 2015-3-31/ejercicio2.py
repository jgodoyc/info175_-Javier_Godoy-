class Vehiculo():
	def __init__(self, bencina, encendido, kilometraje, rendimiento):
		self.bencina = bencina
		self.encendido = encendido
		self.kilometraje = kilometraje
		self.rendimiento = rendimiento
	

	def encender(self):
		if self.encendido == False:
			self.encendido = True
			
	def apagar(self):
		if self.encendido == True:
			self.encendido = False
			
	def Mover(self, kil):
		self.encender()
		bencinaUsada = kil / self.rendimiento
		if self.bencina >= bencinaUsada:
			self.bencina -= bencinaUsada
			self.kilometraje += kil
		else:
			print("No alcanzara a llegar a su destino.")
			self.encendido= False
			print("Se a apagado el Vehiculo")			

	def Obtener_kilometraje(self):
		print("EL kilometraje del Vehiculo es :"+ str(self.kilometraje))

	def Obtener_bencina(self):
		print("La Combustible que hay es: " + str(self.bencina))

	def Cargar_bencina(self, lts):
		self.apagar()
		if lts > 0:
			self.bencina += lts
			print("Combustible total es: " + str(self.bencina))


class Camion(Vehiculo):
	def __init__ (self,bencina, encendido, kilometraje, rendimiento, peso, ruedas, acoplado):
		self.bencina = bencina
		self.encendido = encendido
		self.kilometraje = kilometraje
		self.rendimiento = rendimiento
		self.peso = peso
		self.ruedas = ruedas
		self.acoplado = acoplado

	def agregar_Acoplado(self, peso, ruedas, acoplado):
		self.acoplado.append( [peso, ruedas, acoplado] )

	def quitar_Acoplado(self):
		for i in range(self.acoplado):
			self.acoplado.pop()

	def obtener_Acoplado(self):
		return self.acoplado

	def obtener_Ruedas(self):
		return self.ruedas

	def obtener_Peso(self):
		return self.peso


if __name__ == "__main__":
	camion1 = Camion(0, False, 0, 2.45, 9, 12, [])
	camion1.Obtener_bencina()
	camion1.Cargar_bencina( float(raw_input("Litros de Combustible a cargar: ")) )
	camion1.encender()
	camion1.Mover( float(raw_input("Kilometros que se desea desplazar: ")) )
	camion1.Obtener_kilometraje()
	camion1.Obtener_bencina()
	
