# PROGRAMA DE TABLA MULTIPLICAR DEL 1 AL 10
# RAFAEL ESCALANTE

# Mostrar la tabla de multiplicar para cada número del 1 al 10
for num in range(1, 11):
    print(f"Tabla del {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print()  # Línea en blanco entre tablas
