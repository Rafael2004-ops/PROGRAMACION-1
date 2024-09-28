import cmath

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Calcular el discriminante
discriminante = b**2 - 4*a*c

# Calcular las raíces, permite soluciones complejas
raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
print(f"Las raíces son: {raiz1} y {raiz2}")
