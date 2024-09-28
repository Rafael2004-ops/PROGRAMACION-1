#calcular el indice de masa corporal
import math
#nombre de la persona
nombre = input("Digite su nombre completo")
#ingreso de la edad de la persona
edad = int(input("Digite su numero edad"))
#ingreso del peso en kilogramos de la persona
peso = float(input("Digite su masa en kilogramos"))
#ingreso de altura de la persona en metros
altura = float(input("Digite su altura en metros"))

#formula para calcular el indice de masa corporal
imc = peso / (altura ** 2)
#mostrar resultado
print(imc)




