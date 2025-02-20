import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# 📌 Dataset de ejemplo (puedes usar otro dataset más grande)
texts = [
    "Este producto es increíble, me encantó",  # Positivo
    "No me gustó para nada, muy malo",         # Negativo
    "Es excelente, lo volvería a comprar",     # Positivo
    "Horrible, nunca lo recomendaría",        # Negativo
    "Me gusta mucho, lo uso a diario",        # Positivo
    "Es un desperdicio de dinero",            # Negativo
]

labels = [1, 0, 1, 0, 1, 0]  # 1 = Positivo, 0 = Negativo

# 📌 Tokenización del texto
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# 📌 Padding para que todas las secuencias tengan la misma longitud
max_length = 10
padded_sequences = pad_sequences(sequences, maxlen=max_length, padding="post")

# 📌 Convertir etiquetas a array de numpy
labels = np.array(labels)

# 📌 Definir el modelo
model = keras.Sequential([
    keras.layers.Embedding(input_dim=1000, output_dim=16, input_length=max_length),
    keras.layers.GlobalAveragePooling1D(),
    keras.layers.Dense(16, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")  # 1 salida (Positivo o Negativo)
])

# 📌 Compilar el modelo
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# 📌 Entrenar el modelo
epochs = 10
model.fit(padded_sequences, labels, epochs=epochs, verbose=1)

# 📌 Probar con nuevos textos
new_texts = ["Me encantó este producto", "No me gustó para nada"]
new_sequences = tokenizer.texts_to_sequences(new_texts)
new_padded = pad_sequences(new_sequences, maxlen=max_length, padding="post")

predictions = model.predict(new_padded)

# 📌 Mostrar predicciones
for i, text in enumerate(new_texts):
    print(f"Texto: {text} | Predicción: {'Positivo' if predictions[i] > 0.5 else 'Negativo'}")
