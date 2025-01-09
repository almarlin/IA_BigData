numeros = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

num = int(input("Inserta un número a buscar en la lista: "))

for numero in numeros:
 if numero == num:
  print("Número encontrado")
  break
else:
 print('No se ha encontrado el número')