tot = 0
ex = True

while ex:
    num=int(input(f"La suma actual es {tot}. Si desea finalizar el proceso, introduzca un número negativo: "))
    
    if num < 0:
        break
    tot+=num

print(f"El total asciende a {tot}")