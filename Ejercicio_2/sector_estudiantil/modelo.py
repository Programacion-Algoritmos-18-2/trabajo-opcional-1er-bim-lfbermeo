from personal_academico.modelo import *
class Alumno(object):

	def __init__(self):
		self.nombres = ""
		self.docente_matematica= Docente()
		self.docente_sociales=Docente()
	                		
   #Métodos establecer y obtener de los atributos
	def establecerNombres(self, n):
		self.nombres = n

	def obtenerNombres(self):
		return self.nombres

	def establecerDocenteM(self, a):
		self.docente_matematica = a

	def obtenerDocenteM(self):
		return self.docente_matematica

	def establecerDocenteS(self, e):
		self.docente_sociales = e

	def obtenerDocenteS(self):
		return self.docente_sociales
#con str imprimo y concateno con la clase Docente
	def __str__(self):	
		return "---------------------Reporte-------------\nNombre Alumno:%s\nDocente Matemáticas:\n\t%s\nDocente Sociales:\n\t%s\n"%(self.obtenerNombres(), self.obtenerDocenteM(), self.obtenerDocenteS())