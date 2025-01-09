import random

palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

baraja = [f"{valor} de {palo}" for palo in palos for valor in valores]

random.shuffle(baraja)

cartas_repartidas = [baraja.pop() for _ in range(5)]


print("Las cartas repartidas son:")
for carta in cartas_repartidas:
    print(carta)