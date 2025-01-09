import random

def simular_quiniela():
    resultados = []
    opciones = ["1 (Gana local)", "X (Empate)", "2 (Gana visitante)"]
    
    for _ in range(15):
        resultado = random.choice(opciones)
        resultados.append(resultado)
    
    return resultados


quiniela = simular_quiniela()


print("Resultados de la Quiniela:")
for i, resultado in enumerate(quiniela, start=1):
    print(f"Partido {i}: {resultado}")
