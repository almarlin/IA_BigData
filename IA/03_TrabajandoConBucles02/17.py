char = input("Introduce una letra para saber si es una vocal: ")

char = char.lower()

if char in 'aeiou':
    print("Es una vocal.")
else:
    print("No es una vocal")