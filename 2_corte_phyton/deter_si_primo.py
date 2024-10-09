#ingresar numero que es primo
numero = int(input("ingresar un numero "))
contador = 0

for i in range(1,numero+1):
    if numero % i==0:
        contador = contador+1

if contador == 2:
    print("el numero ingresado es primo")
else:
    print("el numero ingresado No es primo")
