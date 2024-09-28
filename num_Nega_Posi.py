#Realizar un programa que me ingrese un número entero y me diga
#si es positivo o es negativo

#Datos de Entrada
numero = int(input("Ingrese número "))

#Procesamiento
if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es neutro")
else:
    print("El número es negativo")

