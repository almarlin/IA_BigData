import math
def area(rad):
    return math.pi * rad**2

radio = int(input("Introduce el radio: "))

print(f"El área del círculo es: {area(radio)}")