from paquete_1.modelo import *
#De mi clase Equipo todo los valores como es nombre del equipo y al país al que pertenece
equipo1 = Equipo("Necaxa", "México")
equipo2 = Equipo("Lazio", "Italia")
equipo3 = Equipo("Manchester United", "Inglaterra")
#Creo el primer objeto donde le doy valores como lo es el nombre y apellido
f1 = Futbolista("Antonio", "Valencia")
#con el método establecer asigno los valores
f1.establecerEquipo(equipo3)
f1.establecerPosicion("LATERAL")
f1.establecerDorsal(25)
#Imprimo información
print(f1.presentarInformacion())
#segundo objeto
f2 = Futbolista("Alex", "Aguinaga", equipo1, "MEDIOCENTRO")
f2.establecerDorsal(7)
#imprimo
print(f2.presentarInformacion())
#tercer objeto
f3 = Futbolista("Felipe", "Caicedo", equipo2)
f3.establecerPosicion("DELANTERO")
f3.establecerDorsal(32)
#imprimo
print(f3.presentarInformacion())
