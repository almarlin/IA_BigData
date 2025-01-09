def conv(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit

tmp = int(input("Introduce una temperatura: "))

print(f"{tmp} °C = {conv(tmp):.2f} °F")