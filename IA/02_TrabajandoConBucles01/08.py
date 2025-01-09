inicio = int(input("Introduce la temperatura inicial en Celsius: "))
fin = int(input("Introduce la temperatura final en Celsius: "))
incremento = int(input("Introduce el incremento entre cada temperatura: "))

print("Temperaturas en Celsius a Fahrenheit:")

for celsius in range(inicio, fin + 1, incremento):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} °C = {fahrenheit:.2f} °F")