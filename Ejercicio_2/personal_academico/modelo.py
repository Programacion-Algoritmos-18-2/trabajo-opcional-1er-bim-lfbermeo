class Docente(object):
    
	def __init__(self):
		self.nombre = ""
		self.apellido=""
		self.titulo=""
	 #metodos establecer y obetener de los atributos               		
	def establecerNombre(self, n):
		self.nombre = n

	def obtenerNombre(self):
		return self.nombre

	def establecerApellido(self, a):
		self.apellido = a

	def obtenerApellido(self):
		return self.apellido

	def establecerTitulo(self, e):
		self.titulo = e

	def obtenerTitulo(self):
		return self.titulo
#con str imprimo los datos que necesito
	def __str__(self):
		return "Nombre: %s\tApellido: %s\tTitulo: %s"%(self.obtenerNombre(),self.obtenerApellido(), self.obtenerTitulo()) 
		