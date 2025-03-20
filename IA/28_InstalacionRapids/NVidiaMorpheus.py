# Descargar la imagen:
# $ docker pull nvcr.io/nvidia/morpheus/morpheus:25.02-runtime
# Poner en marcha el contenedor:
# $ docker run --rm -ti --runtime=nvidia --gpus=all --net=host \ -v /mnt/c/Users/alumno/Desktop/Alvaro_IABIGDATA/IA_BigData/IA/28_InstalacionRapids/:/workspace/data \ nvcr.io/nvidia/morpheus/morpheus:25.02-runtime bash
# El uso de NVidia Morpheus no contempla el entrenamiento de modelos. Está enfocado a la seguridad. El ejemplo siguiente es mejor para determinar el correcto funcionamiento.

import morpheus
import numpy as np
import cupy as cp

# Crea algunos datos de entrada
data = np.random.rand(1000, 300).astype(np.float32)

# Convierte los datos a CuPy para usar la GPU
gpu_data = cp.asarray(data)

# Realiza una inferencia con Morpheus (esto es solo un ejemplo básico)
output = morpheus.some_inference_function(gpu_data)

print(output)

# import cudf
# from cuml.ensemble import RandomForestClassifier
# from cuml.preprocessing import StandardScaler
# from cuml.metrics import accuracy_score, confusion_matrix
# from sklearn.model_selection import train_test_split
# import numpy as np

# # 1. Cargar datos (ejemplo sintético similar al dataset CIC-IDS2017)
# # Generar datos de tráfico normal y anómalo
# n_samples_normal = 100_000
# n_samples_attack = 10_000

# # Características: duración, protocolo, puerto, bytes transferidos
# normal_traffic = cudf.DataFrame({
#     "duration": np.random.normal(10, 2, n_samples_normal),
#     "protocol": np.random.choice([6, 17], n_samples_normal),  # TCP=6, UDP=17
#     "port": np.random.randint(80, 443, n_samples_normal),
#     "bytes": np.random.normal(500, 100, n_samples_normal),
#     "label": 0  # Tráfico normal
# })

# attack_traffic = cudf.DataFrame({
#     "duration": np.random.exponential(20, n_samples_attack),
#     "protocol": np.random.choice([6, 17], n_samples_attack),
#     "port": np.random.randint(0, 1024, n_samples_attack),
#     "bytes": np.random.normal(2000, 500, n_samples_attack),
#     "label": 1  # Ataque
# })

# # Combinar datos
# data = cudf.concat([normal_traffic, attack_traffic])
# X = data.drop("label", axis=1)
# y = data["label"]

# # 2. Preprocesamiento
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # Dividir datos
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# # 3. Entrenar modelo (Random Forest en GPU)
# model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
# model.fit(X_train, y_train)

# # 4. Evaluar modelo
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# conf_matrix = confusion_matrix(y_test, y_pred)

# print(f"Accuracy: {accuracy:.4f}")
# print("Matriz de confusión:\n", conf_matrix.toarray())
