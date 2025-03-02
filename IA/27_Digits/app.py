from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import tensorflow as tf
from io import BytesIO
import base64

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

    # Decodificar la imagen base64 (eliminar la cabecera)
    image_data = image_data.split(",")[1]  # Eliminar la cabecera de base64
    
    # Comprobar la longitud de los datos decodificados
    decoded_image = base64.b64decode(image_data)
    print(f"Longitud de los datos de imagen decodificados: {len(decoded_image)}")

    # Intentar abrir la imagen decodificada
    try:
        image = Image.open(BytesIO(decoded_image))
        # Mostrar la imagen (si es posible)
        # image.show()
    except Exception as e:
        return jsonify({'error': f"Error al abrir la imagen: {str(e)}"}), 400
    
    # Verificar el tamaño de la imagen original
    print(f"Tamaño original de la imagen: {image.size}")

    # Redimensionar la imagen al tamaño 28x28
    image = image.resize((28, 28))  # Redimensionar a 28x28 píxeles

    # Verificar el tamaño de la imagen después de redimensionar
    print(f"Tamaño de la imagen después de redimensionar: {image.size}")

    # Convertir la imagen a un array de numpy
    image_array = np.array(image)

    # Mostrar los valores de los píxeles
    print(f"Valores de los píxeles después de redimensionar: {image_array.min()} a {image_array.max()}")
    print(f"Forma de la imagen después de convertir a array: {image_array.shape}")

    # Verificar si la imagen tiene valores válidos antes de continuar
    if np.all(image_array == 0):
        return jsonify({'error': "La imagen no contiene información válida"}), 400

    # Normalizar la imagen (debe estar entre 0 y 1)
    image_array = image_array / 255.0

    # Invertir los colores (fondo blanco, dígito negro) después de normalizar
    image_array = 1 - image_array  # Invertir colores

    # Cambiar la forma de la imagen a (1, 28, 28, 1)
    image_array = image_array.reshape(1, 28, 28, 1)

    debug_image = (image_array[0, :, :, 0] * 255).astype(np.uint8)  # Desnormalizar y convertir a uint8
    Image.fromarray(debug_image).save('debug_image.png')  # Guardar la imagen

    # Hacer la predicción con el modelo
    prediction = model.predict(image_array)
    predicted_digit = np.argmax(prediction)  # Obtener el índice de la clase con mayor probabilidad

    # Convertir el dígito predicho a tipo int para asegurarnos de que sea serializable en JSON
    predicted_digit = int(predicted_digit)

    # Retornar la predicción en formato JSON
    return jsonify({'prediction': predicted_digit})

if __name__ == '__main__':
    app.run(debug=True)
