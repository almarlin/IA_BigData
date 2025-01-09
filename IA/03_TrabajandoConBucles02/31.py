palabraOrg =input("Introduce una palabra para comprobar si es un palíndromo: ")
palabra = palabraOrg.lower()

inicio = 0
fin = len(palabra)-1

palindromo = True

while inicio < fin:
    if palabra[inicio]!=palabra[fin]:
        palindromo=False
        break
    inicio+=1
    fin-=1

if palindromo:
    print(f"{palabraOrg} es un palíndromo")
else:
    print(f"{palabraOrg} no es un palíndromo")