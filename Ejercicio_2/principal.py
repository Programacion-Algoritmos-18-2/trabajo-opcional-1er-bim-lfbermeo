from personal_academico.modelo import *
from sector_estudiantil.modelo import *
#Creo el objeto alumno
a = Alumno()
#Con la palabra reservada input ingresar datos por teclado
a.establecerNombres(input("Ingrese nombre alumno: "))
#Creo el segundo objeto tipo docente
d1 = Docente()
#datos por teclado
d1.establecerNombre(input("Ingrese nombre Docente1: "))
d1.establecerApellido(input("Ingrese apellido Docente1: "))
d1.establecerTitulo(input("Ingrese titulo Docente1: "))
#cre el tercer obejto tipo docente
d2 = Docente()
#datos por teclado
d2.establecerNombre(input("Ingrese nombre Docente2: "))
d2.establecerApellido(input("Ingrese apellido Docente2: "))
d2.establecerTitulo(input("Ingrese titulo Docente2: "))
#le doy los valores de tipo almuno a Docente
a.establecerDocenteM(d1)
a.establecerDocenteS(d2)
#Imprimo con el método str
print(a)
