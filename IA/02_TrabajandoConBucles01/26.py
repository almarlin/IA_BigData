niveles = int(input("Introduce el número de niveles de la pirámide: "))

for i in range(1, niveles + 1):
    print(' ' * (niveles - i), end='')  
    for j in range(1, i + 1):
        print(j, end=' ') 
    print()
