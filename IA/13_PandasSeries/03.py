import pandas as pd
import matplotlib.pyplot as plt

semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
data = []
print("\nIntroduce las temperaturas de la semana:\n")

for dia in semana:
    data.append(float(input(f"Temperatura del {dia}:\n")))
    
temps = pd.Series(data,semana)

print(f"Temperatura máxima: {temps.max()} el {temps.idxmax()}")
print(f"Temperatura mínima: {temps.min()} el {temps.idxmin()}")

tempsMayor = temps[temps > 25]

print(f"Temperaturas mayores a 25º\n{tempsMayor}")

temps = temps.fillna(temps.mean())

plt.figure(figsize=(10,6))
temps.plot()
plt.title("Temperaturas de la semana")
plt.xlabel("Día de la semana")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.xticks(rotation=45)
plt.show()