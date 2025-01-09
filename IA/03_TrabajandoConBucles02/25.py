cadena = input("Introduce una cadena: ")

dig = 0
char = 0

for i in cadena:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char += 1

print(f"En la cadena hay {dig} números y {char} caracteres.")

