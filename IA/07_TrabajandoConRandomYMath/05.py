import random

def calcularValor(cartas):
    valor = 0
    ases = 0
    
    for carta, _ in cartas:
        if carta in ['J', 'Q', 'K']:
            valor += 10
        elif carta == 'A':
            valor += 11
            ases += 1
        else:
            valor += int(carta)
    
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    
    return valor

palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

baraja = [(valor,palo) for palo in palos for valor in valores]

random.shuffle(baraja)

# cartas_repartidas = [baraja.pop() for _ in range(5)]

cartasMesa = [baraja.pop() for _ in range(2)]
cartasJugador = [baraja.pop() for _ in range(2)]

print(f"El dealer tiene {cartasMesa[0]} como carta visible")

while True:
    jugar = True
    for valor, palo in cartasJugador:
        print(f"{valor} de {palo}")
    print(f"jugador suma total: {calcularValor(cartasJugador)}")

    dec = input("¿Quieres otra carta? s/n\n")
    
    if dec == 's':
        cartasJugador.append(baraja.pop())
    else:
        break
    

    if calcularValor(cartasJugador) > 21:
        print("¡Te has pasado! Has perdido")
        jugar = False
        break

if jugar == True:
    while True:
        for valor, palo in cartasMesa:
            print(f"{valor} de {palo}")
        
        print(f"Dealer suma total: {calcularValor(cartasMesa)}")
        

        if calcularValor(cartasMesa) > 21:
            print("¡Se ha pasado! ¡Has ganado!")
            break
        elif calcularValor(cartasMesa) >= calcularValor(cartasJugador):
            print("¡Has perdido!")
            break
        elif calcularValor(cartasMesa) < calcularValor(cartasJugador) and calcularValor(cartasMesa) <= 16:
            cartasMesa.append(baraja.pop())
        else:
            print(f"El dealer se planta con {calcularValor(cartasMesa)}. ¡Has ganado!")
            break