class Futbolista(object):
     #Creamos el contructor asinandole valores por defecto, para poder llenar los valores del objeto en el método main   
	def __init__(self, nombre="", apellido="", equipo=None, posicion="",dorsal=0):
				self.establecerNombre(nombre)
				self.establecerApellido(apellido)
				self.establecerEquipo(equipo)
				self.establecerPosicion(posicion)
				self.establecerDorsal(dorsal)

 		                      		                		
    #métodos establecer y obtener para cada una de las variables
	def establecerNombre(self, n):
		self.nombre = n

	def obtenerNombre(self):
		return self.nombre

	def establecerApellido(self, a):
		self.apellido = a

	def obtenerApellido(self):
		return self.apellido

	def establecerEquipo(self, e):
		self.equipo = e

	def obtenerEquipo(self):
		return self.equipo

	def establecerPosicion(self, p):
		self.posicion = p

	def obtenerPosicion(self):
		return self.posicion
	
	def establecerDorsal(self, d):
		self.dorsal = d

	def obtenerDorsal(self):
		return self.dorsal	
	#Presento información que necesito
	def presentarInformacion(self):
		cadena = "Jugador: \n\t\t%s %s,\n\t\tPertenece al equipo %s,\n\t\tsu posicion es %s y,\n\t\tsu dorsal es el número %s.\n"%(self.obtenerNombre(), self.obtenerApellido(), self.equipo.obtenerDatos(), self.obtenerPosicion(), self.obtenerDorsal())
		return cadena	
#creó la segunda clase
class Equipo(object):
	#el contructor tiene los valores como lo es el nombre y pais
	def __init__(self, nombre_equipo, pais):

		self.nombre_equipo= nombre_equipo
		self.pais = pais
		#Métodos establecer y obtener de los dos atributos
	def establecerNomEquipo(self, n_e):
		self.nombre_equipo = n_e

	def obtenerNomEquipo(self):
		return self.nombre_equipp
	
	def establecerPais(self, p):
		self.pais = p

	def obtenerPais(self):
		return self.pais
	#obtengo la información para poder presentar la información
	def obtenerDatos(self):
		return self.nombre_equipo + " del pais " + self.pais

		