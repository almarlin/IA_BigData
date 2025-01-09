def distRec(pasos):
    metros = pasos * 0.78
    km = metros / 1000
    return km

p = int(input("Introduce los pasos: "))
print(f"El total de KM recorridos son: {distRec(p)}")
