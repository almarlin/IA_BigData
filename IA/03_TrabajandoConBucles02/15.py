anyo = int(input("Introduce un año: "))

if anyo%4 == 0:
    print(f"El año {anyo} es bisiesto")
else:
    print(f"El año {anyo} no es bisiesto")