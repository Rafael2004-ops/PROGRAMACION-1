import math
#datos de entrada
a = int(input("ingrese el coeficiente a "))
b = int(input("ingrese el coeficiente b "))
c = int(input("ingrese el coeficiente c" ))
#procedimiento
raiz1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
raiz2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
#salida
print("la raiz uno es: ", raiz1)
print("la raiz dos es: ", raiz2)