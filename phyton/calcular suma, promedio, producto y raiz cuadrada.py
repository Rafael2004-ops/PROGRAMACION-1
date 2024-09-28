#Calcular la suma, el producto, el promedio y la raiz cuadrada.
import math

#Es la variable del numero uno
numerouno = int(input("digite el numero uno "))
#Es la variable del numero dos
numerodos = int(input("digite el numero dos "))
#Es la variable del numero tres
numerotres = int(input("digite el numero tres "))
#Es la variable del numero cuatro
numerocuatro = int(input("digite el numero cuatro "))
#Es la variable del numero cinco 
numerocinco = int(input("digite el numero cinco "))

#Es la variable operacion de suma de todos los numeros
suma = numerouno + numerodos + numerotres + numerocuatro + numerocinco
#Es la variable operacion del promedio de todos los numeros
promedio = (numerouno + numerodos + numerotres + numerocuatro + numerocinco)/5
#Es la variable operacion del producto de todos los numeros
producto = numerouno * numerodos * numerotres *numerocuatro * numerocinco
#Es la variable de la raiz cuadrada
raizcuadrada = math.sqrt(promedio) 

#orden de los resultados
print(suma)
print(promedio)
print(producto)
print(raizcuadrada)






