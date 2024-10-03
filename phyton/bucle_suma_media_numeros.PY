#progrmaque me pida numeros hasta que ingrese un cero
#rafal escalante
#suma, cantidad media de los numeros ingresados

num = int(input("ingrese un numero: "))
acumulador = 0
contador = 0

while(num>0):
    acumulador = acumulador+num
    contador = contador+1
    num = int(input("ingrese un numero"))

print("la suma es: ", acumulador)
print("la cantidad de numeros es: ",contador)
print("la media de los numeros es: ",(acumulador/contador))



