#Realizar un programa que me ingrese tres números y me calcule la suma de sus cubos.
#numero
Nem1=int(input("ingrese un numero"))
Nem2=int(input("ingrese un numero"))
Nem3=int(input("ingrese un numero"))
#cubo
cubo1=Nem1**3
cubo2=Nem2**3
cubo3=Nem3**3

suma=cubo1+cubo2+cubo3

print("cubo del primer numero", cubo1)
print("cubo del segundo numero", cubo2)
print("cubo del terce numero", cubo3)
print("la suma suma de los cubos es", suma)
