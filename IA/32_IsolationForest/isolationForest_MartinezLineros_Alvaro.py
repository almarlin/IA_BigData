import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# 1. Generar datos simulados de transacciones bancarias
np.random.seed(42)

# Simulamos 1000 transacciones:
# 950 son "normales" y 50 son fraudulentas (anomalías).
normal_transactions = np.random.normal(
    loc=200, scale=50, size=(950, 2)
)  # Normal: Monto, Tiempo
fraudulent_transactions = np.random.normal(
    loc=600, scale=150, size=(50, 2)
)  # Fraudulentas

# Concatenar los datos en un solo dataset
transactions = np.vstack([normal_transactions, fraudulent_transactions])
labels = np.array([0] * 950 + [1] * 50)  # 0 = normal, 1 = fraudulento

# Convertimos a DataFrame
df = pd.DataFrame(transactions, columns=["Amount", "Time"])
df["Label"] = labels

df.to_csv("transacciones.csv")
# 2. Escalar los datos
scaler = StandardScaler()
transactions_scaled = scaler.fit_transform(df[["Amount", "Time"]])

# 3. Aplicar Isolation Forest
iso_forest = IsolationForest(
    random_state=42, contamination=0.1, n_estimators=100, max_samples=10
)

iso_forest.fit(transactions_scaled)

# Predecir las anomalías (1: normal, -1: anomalía)
df["Anomaly"] = iso_forest.predict(transactions_scaled)

# 4. Identificar las transacciones con mayor probabilidad de fraude
fraud_transactions = df[df["Anomaly"] == -1]


# 5. Visualizar las anomalías en un gráfico
plt.figure(figsize=(10, 6))
plt.scatter(
    df["Amount"], df["Time"], c=df["Anomaly"], cmap="coolwarm", label="Transacciones"
)
plt.scatter(
    fraud_transactions["Amount"],
    fraud_transactions["Time"],
    color="red",
    label="Anomalías",
    marker="x",
)
plt.title("Detección de Anomalías en Transacciones Bancarias")
plt.xlabel("Monto")
plt.ylabel("Tiempo")
plt.legend()
plt.show()

# --------------------------------------------------------------------------
# ¿Cómo varía el umbral de detección con diferentes hiperparámetros?
# Los hiperparámetros que afectan al umbral de detección son:
# 1. 'contamination': Este parámetro especifica la fracción de puntos que se espera que sean anomalías.
#    Si aumentamos la contaminación, el modelo se vuelve más permisivo y detecta más puntos como anomalías.
# 2. 'n_estimators': Este parámetro controla el número de árboles en el bosque. Aumentar este número puede mejorar la precisión del modelo,
#    pero también aumenta el tiempo de cómputo.
# 3. 'max_samples': Este parámetro controla el número de muestras que se utilizan para entrenar cada árbol.
#    Si es muy pequeño, el modelo puede ser menos preciso.
