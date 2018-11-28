from paquete_1.modelo import *
#objeto para los atribuots de garante
g1 = Garante()
g1.establecerNombre("José")
g1.establecerApellido("Ramirez")
g1.establecerSueldo(765.4)
#segundo objeto tipo garante para llenar atributos
g2 = Garante()
g2.establecerNombre("Camila")
g2.establecerApellido("Salazar")
g2.establecerSueldo(1000.40)
#tercer objeto tipo prestamo para establer los datos que necesito
prestamo = Prestamo()
prestamo.establecerGarante1(g1)
prestamo.establecerNombreBene("Pedro")
prestamo.establecerMontoP(70.765)
prestamo.establecerInteres(20)
prestamo.establecerTiempoPrestamo(10)
#cuarto objeto tipo prestamo automovil para establecer los datos qeu necesito
prestamoAutomovil = PrestamosAutomovil()
prestamoAutomovil.establecerGarante1(g1)
prestamoAutomovil.establecerGarante2(g2)
prestamoAutomovil.establecerNombreBene("Edison")
prestamoAutomovil.establecerMontoP(50.450)
prestamoAutomovil.establecerInteres(20)
prestamoAutomovil.establecerTiempoPrestamo(8)
prestamoAutomovil.establecerTipoVehiculo("Auto")
prestamoAutomovil.establecerMarcaVehiculo("Ford")
#imprimo los datos
print(prestamo)
print(prestamoAutomovil)
