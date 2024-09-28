#Escribir un programa que me ingrese el radio de  la base y la altura de un cilindro,
#me calcule el volumen del cilindro que es a partir de la siguiente ecuación.
#V = PI*r^2*h

#Datos de Entrada
import math
radiobase = int(input("Digite el radio de la base del cilindro "))
altura = int(input("Digite la altura del cilindro "))

#Procesamiento
volumen = math.pi*radiobase**2*altura 
volumen1 = (math.pi)*(math.pow(radiobase,2))*altura

#Datos de Salida
print("Volumen del Cilindro es ", volumen, volumen1)
