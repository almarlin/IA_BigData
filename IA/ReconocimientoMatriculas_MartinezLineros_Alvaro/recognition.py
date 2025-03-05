import cv2
import pytesseract
import re

# Configurar el path de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\alumno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Función para preprocesar la imagen (convertir a escala de grises y aplicar umbral)
def preprocess_image(image_path):
    # Cargar la imagen
    image = cv2.imread(image_path)
    
    # Convertir a escala de grises
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar un umbral para convertir la imagen a blanco y negro
    _, thresh = cv2.threshold(image_gray, 150, 255, cv2.THRESH_BINARY)

    # Eliminar ruido con un filtro GaussianBlur
    blur = cv2.GaussianBlur(thresh, (5, 5), 0)

    return blur, image  # Devuelvo también la imagen original para poder dibujar en ella

# Función para extraer matrículas (buscando múltiples áreas de texto)
def recognise(filepath):
    # Preprocesar la imagen
    preprocessed_image, original_image = preprocess_image(filepath)

    # Detectar contornos en la imagen preprocesada
    contours, _ = cv2.findContours(preprocessed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Lista para almacenar las matrículas detectadas
    license_plates = []

    # Iterar sobre los contornos encontrados
    for contour in contours:
        # Ignorar contornos pequeños que no sean relevantes (ajustar según sea necesario)
        if cv2.contourArea(contour) < 500:
            continue
        
        # Obtener las coordenadas del rectángulo delimitador
        x, y, w, h = cv2.boundingRect(contour)

        # Extraer la región de interés (ROI) de la imagen original
        roi = original_image[y:y+h, x:x+w]

        # Usar Tesseract para extraer el texto de la ROI (posible matrícula)
        custom_config = r'--psm 8 --oem 3'  # Usar psm 8 si cada contorno es una línea de texto
        text = pytesseract.image_to_string(roi, config=custom_config)

        # Filtrar el texto para eliminar caracteres especiales
        text = re.sub(r'[^A-Za-z0-9\s]', '', text)  # Elimina caracteres especiales
        text = text.strip()
        # Validar si el texto extraído podría ser una matrícula (ajustar según el formato)
        if re.match(r'[0-9]{4} [A-Za-z]{2}', text):  # Ejemplo para matrículas tipo 2L-4N-2L
            license_plates.append(text.strip())

    return license_plates

