cad = input("Introduce una cadena con letras y numeros: ")

dig=0
let=0

for i in range(0,len(cad)):
    if cad[i].isdigit():
        dig+=1
    else:
        let+=1


print(f"Letras: {let} Digitos: {dig}")