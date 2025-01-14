import matplotlib.pyplot as plt

# Principalmente para mostrar diagramas (barras, histogramas, sectores, caja y bigote, etc.)
#  pip install matplotlib

x = ["A", "B", "C", "D", "E"]
y = [23, 56, 23, 65, 86]

plt.bar(x, y)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfico de barras")
plt.show()
