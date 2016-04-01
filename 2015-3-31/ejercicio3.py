class persona():
	def __init__(self, rut, nombre, nacimiento, sexo):
		self.rut = rut
		self.nombre = nombre
		self.nacimiento = nacimiento
		self.sexo = sexo

	def obtener_edad(self):
		return self.nacimiento
class nota():
	def __init__(self, valor, ponderarcion, ramo, carrera):
		self.valor = valor
		self.ponderarcion = ponderarcion
		self.ramo = ramo
		self.carrera = carrera

	def obtener_valor(self):
		return self.valor
	def obtener_ponderaion(self):
		return self.ponderarcion
	def modificar(self):
		return self.modificar

class alumno(persona):
	def __init__(self, rut, nombre, nacimiento, sexo, correo, carrera, promocion, notas):
		self.rut = rut
		self.nombre = nombre
		self.nacimiento = nacimiento
		self.sexo = sexo
		self.correo = correo
		self.carrera = carrera
		self.promocion = promocion
		self.notas = []
	def agregar_nota(self, notas):
		return self.notas
	def PGA(self, prom):
		for i in self.notas[]:
			promg += self.promedio_ramo
		promg = promg/len(self.notas[])
		return self.prom_general
	def promedio_ramo(self, notas, ramo):
		return self.promedio_ramo

if __name__ == "__main__":
	alumno1 = alumno(18283788, "javier", "22 abril", "H", "jgodoyc@hotmail.com", 1, 2014, [5.0, 6.1,3.6, 4.5]):

	
