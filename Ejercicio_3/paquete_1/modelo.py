class Garante(object):
	def __init__(self):
		#atributos
		self.nombre = ""
		self.apellido = ""
		self.sueldo= 0.0
		#metodos establecer y obtener de mis atributos
	def establecerNombre(self, n):
		self.nombre = n

	def obtenerNombre(self):
		return self.nombre

	def establecerApellido(self, a):
		self.apellido = a

	def obtenerApellido(self):
		return self.apellido

	def establecerSueldo(self, s):
		self.sueldo = s

	def obtenerSueldo(self):
		return self.sueldo
		#Con el método str imprimo los datos del garante, tanto para el garante 1 y 2
	def __str__(self):
		return "Nombre:%s Apellido:%s Sueldo:%.2f"%(self.obtenerNombre(), self.obtenerApellido(), self.obtenerSueldo())	
class Prestamo(object):
	def __init__(self):
		#atributos de la calse
		self.nombreBene = ""
		self.montoPrestamo = 0.0
		self.interes = 0.0
		self.tiempoPrestamoAnios = 0
		self.garante1= Garante()
		#metodos establecer y obtener de los atributos
	def establecerNombreBene(self, n):
		self.nombre = n

	def obtenerNombreBene(self):
		return self.nombre

	def establecerMontoP(self, s):
		self.montoPrestamo = s

	def obtenerMontoP(self):
		return self.montoPrestamo	

	def establecerInteres(self, n):
		self.interes = n

	def obtenerInteres(self):
		return self.interes

	def establecerTiempoPrestamo(self, a):
		self.tiempoPrestamoAnios = a

	def obtenerTiempoPrestamo(self):
		return self.tiempoPrestamoAnios

	def establecerGarante1(self, s):
		self.garante1 = s

	def obtenerGarante1(self):
		return self.garante1
#con el método str impri mo mi reporte
	def __str__(self):
		return "--------REPORTE-------\nNombre beneficiario:%s Monto Prestamo:%.2f Interes:%.2f%% Tiempo de prestamos Años:%d\nGarante:%s\n" %(self.obtenerNombreBene(), self.obtenerMontoP(), self.obtenerInteres(), self.obtenerTiempoPrestamo(), self.obtenerGarante1())
#Clase que hereda atributos de Prestamo
class PrestamosAutomovil(Prestamo):
	def __init__(self):
		super(PrestamosAutomovil, self).__init__()
		#atributos
		self.tipoVehiculo= ""
		self.marcaVehiculo= ""
		self.garante2 = Garante()
		#métodos establecer y obtener para los atributos
	def establecerTipoVehiculo(self, n):
		self.tipoVehiculo = n

	def obtenerTipoVehiculo(self):
		return self.tipoVehiculo

	def establecerMarcaVehiculo(self, a):
		self.marcaVehiculo = a

	def obtenerMarcaVehiculo(self):
		return self.marcaVehiculo

	def establecerGarante2(self, s):
		self.garante2 = s

	def obtenerGarante2(self):
		return self.garante2
#método str para que imprima los datos 
	def __str__(self):

		return "%sTipo de vehiculo:%s  Marca vehiculo:%s\n Garante 2:%s\n"%(super(PrestamosAutomovil, self).__str__(),self.obtenerTipoVehiculo(),self.obtenerMarcaVehiculo(),self.obtenerGarante2())			 			


		