cadena = input("Inserta una cadena para ser invertida: ")

final = ""

for c in cadena:
    final = c + final

print(f"La cadena invertida es: {final}")