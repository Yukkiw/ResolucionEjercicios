class velocidad():
    velocidad = 100

class cilindrada():
    cilindrada = 4

class vehiculo:
    velocidad = velocidad()
    cilindrada = cilindrada()

class ruedas():
    cantidad = 4

class puertas():
    cantidad = 2

class color():
    color = "Azul"

class coche():
    ruedas = ruedas()
    puertas = puertas()
    color = color()
    vehiculo = vehiculo()

c = coche()
print("Coche es de color", c.color.color)
print("Puertas del coche:", c.puertas.cantidad)
print("Ruedas del coche:", c.ruedas.cantidad)
print("La velocidad del coche es :", c.vehiculo.velocidad.velocidad)
print("La cilindrada del coche es :", c.vehiculo.cilindrada.cilindrada)