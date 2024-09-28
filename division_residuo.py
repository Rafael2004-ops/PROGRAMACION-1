#Escribir un programa que me permita ingresar dos numeros que me calcule el dividendo,
#el divisor, el cociente y el resto (residuo).

#Datos de Entrada
numerouno = int(input("Ingrese el número uno "))
numerodos = int(input("Ingrese el número dos "))
#numerouno/numerodos

#Procesamiento
dividendo = numerouno
divisor = numerodos
cociente = numerouno/numerodos
cocienteotraforma = numerouno//numerodos
resto = numerouno%numerodos

#Datos de Salida
print("Dividendo ", dividendo)
print("Divisor ", divisor)
print("Cociente ", cociente, cocienteotraforma)
print("Resto ", resto)

