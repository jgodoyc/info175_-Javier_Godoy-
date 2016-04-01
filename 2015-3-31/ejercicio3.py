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
	def __init__(self, correo, carrera, promocion, notas):
		self.correo = correo
		self.carrera = carrera
		self.promocion = promocion
		self.notas = notas
	def agregar_nota(self):
		return self.notas
	def PGA(self):
		return self.prom_general
	def promedio_ramo(self, ):
		return self.promedio_ramo

