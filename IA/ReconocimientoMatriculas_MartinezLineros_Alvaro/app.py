import os
from flask import Flask, request, render_template
from recognition import recognise

app = Flask(__name__)

# Definir la ruta de carga de archivos
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Se comprueba que venga un archivo en la petición
    if 'file' not in request.files:
        return 'Sin archivos', 400

    # Recuperar el archivo enviado
    file = request.files['file']
    
    # Crear la ruta completa para guardar el archivo
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    
    # Guardar el archivo
    file.save(filepath)

    # Llamar a la función de reconocimiento de matrícula
    license = recognise(filepath)

    return render_template('index.html', license=license, image_file=file.filename)

if __name__ == '__main__':
    app.run(debug=True)
