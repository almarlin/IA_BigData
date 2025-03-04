from flask import Flask, request, jsonify, send_file
import numpy as np
from PIL import Image
import tensorflow as tf
from io import BytesIO
import base64
import os

# Cargar el modelo de TensorFlow
model = tf.keras.models.load_model('mymodel.keras')

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    image_data = data['image']

    # Imprimir los primeros caracteres de la cadena base64 para verificar su formato
    print(f"Primeros 100 caracteres de la base64 recibida: {image_data[:100]}")

    # Decodificar la imagen base64 (eliminar la cabecera)
    image_data = image_data.split(",")[1]  # Eliminar la cabecera de base64
    
    # Comprobar la longitud de los datos decodificados
    decoded_image = base64.b64decode(image_data)
    print(f"Longitud de los datos de imagen decodificados: {len(decoded_image)}")

    # Intentar abrir la imagen decodificada
    try:
        image = Image.open(BytesIO(decoded_image))

        # Si tiene un fondo transparente (RGBA), llenarlo con blanco
        if image.mode == 'RGBA':
            # Crear una nueva imagen RGB de fondo blanco
            background = Image.new("RGB", image.size, (255, 255, 255))  # Fondo blanco
            background.paste(image, (0, 0), image)  # Pegar la imagen sobre el fondo blanco
            image = background  # Asignar la imagen modificada al objeto image
    except Exception as e:
        return jsonify({'error': f"Error al abrir la imagen: {str(e)}"}), 400
    image = image.convert("L")  # Convertir la imagen a escala de grises
    # Verificar el tamaño de la imagen original
    print(f"Tamaño original de la imagen: {image.size}")

    # Redimensionar la imagen al tamaño 28x28
    image = image.resize((28, 28))  # Redimensionar a 28x28 píxeles

    # Verificar el tamaño de la imagen después de redimensionar
    print(f"Tamaño de la imagen después de redimensionar: {image.size}")

    # Convertir la imagen a un array de numpy
    image_array = np.array(image)

    # Mostrar los valores de los píxeles antes de la normalización
    print(f"Valores de los píxeles antes de normalización: {image_array.min()} a {image_array.max()}")
    print(f"Forma de la imagen después de convertir a array: {image_array.shape}")

    # Verificar si la imagen tiene valores válidos antes de continuar
    if np.all(image_array == 0):
        return jsonify({'error': "La imagen no contiene información válida"}), 400

    # Invertimos los colores de la imagen
    image_array = 1.0 - image_array / 255.0

    # Mostrar los valores de los píxeles después de la normalización
    print(f"Valores de los píxeles después de normalización: {image_array.min()} a {image_array.max()}")

    # Cambiar la forma de la imagen a (1, 28, 28, 1) - Asegúrate de que tiene la forma correcta
    image_array = image_array.reshape(1, 28, 28, 1)  # Asegurarse de que la imagen tenga 1 canal (escala de grises)

    # Hacer la predicción con el modelo
    prediction = model.predict(image_array)
    predicted_digit = np.argmax(prediction)  # Obtener el índice de la clase con mayor probabilidad
    # Guardar la imagen redimensionada y procesada antes de hacer la predicción
    image.save("processed_image.png")
    print("Imagen procesada guardada como 'processed_image.png'")

    # Convertir el dígito predicho a tipo int para asegurarnos de que sea serializable en JSON
    predicted_digit = int(predicted_digit)
    print(f"Probabilidades: {prediction}") 
    print(f"Probabilidades: {predicted_digit}")
    # Retornar la predicción en formato JSON
    return jsonify({'prediction': predicted_digit})

if __name__ == '__main__':
    app.run(debug=True)
