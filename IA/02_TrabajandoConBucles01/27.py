import random

cara_consecutivas = 0
lanzamientos = 0

while cara_consecutivas < 3:
    lanzamiento = random.randint(0, 1)
    lanzamientos += 1 

    if lanzamiento == 1:  
        cara_consecutivas += 1  
        print("Lanzamiento:", lanzamientos, "- Cara")
    else:
        cara_consecutivas = 0  
        print("Lanzamiento:", lanzamientos, "- Cruz")


print(f"\n¡Se obtuvieron 3 caras consecutivas después de {lanzamientos} lanzamientos!")
