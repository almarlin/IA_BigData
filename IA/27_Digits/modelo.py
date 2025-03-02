import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Cargar el conjunto de datos MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocesamiento de las imágenes (normalización y redimensionamiento)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalizar las imágenes

# Construir el modelo convolucional
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),  # Capa convolucional
    layers.MaxPooling2D((2, 2)),  # Capa de pooling
    layers.Conv2D(64, (3, 3), activation='relu'),  # Segunda capa convolucional
    layers.MaxPooling2D((2, 2)),  # Segunda capa de pooling
    layers.Flatten(),  # Aplanar la salida para conectarla a capas densas
    layers.Dense(128, activation='relu'),  # Capa densa
    layers.Dropout(0.5),  # Capa de abandono para evitar el sobreajuste
    layers.Dense(10, activation='softmax')  # Capa de salida con 10 neuronas (una por cada dígito)
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Evaluar el modelo
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Test accuracy: {test_acc}")

# Guardar el modelo
model.save("mymodel.keras")