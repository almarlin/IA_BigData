const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        const clearBtn = document.getElementById('clear-btn');
        const predictionText = document.getElementById('prediction');

        // Configuración para dibujar en el canvas
        let isDrawing = false;
        let lastX = 0;
        let lastY = 0;

        canvas.addEventListener('mousedown', (e) => {
            isDrawing = true;
            [lastX, lastY] = [e.offsetX, e.offsetY];
        });

        canvas.addEventListener('mousemove', (e) => {
            if (!isDrawing) return;
            ctx.beginPath();
            ctx.moveTo(lastX, lastY);
            ctx.lineTo(e.offsetX, e.offsetY);
            ctx.stroke();
            [lastX, lastY] = [e.offsetX, e.offsetY];
        });

        canvas.addEventListener('mouseup', () => {
            isDrawing = false;
            sendCanvasData();
        });

        clearBtn.addEventListener('click', () => {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            predictionText.textContent = '';
        });

        // Función para enviar los datos del canvas al backend
        function sendCanvasData() {
            // Captura la imagen del canvas en formato base64
            const imageData = canvas.toDataURL('image/png');
        
            // Muestra la imagen capturada en una etiqueta <img> para verificación
            const debugImage = document.getElementById('debug-image');
            debugImage.src = imageData;
        
            // Envía la imagen al backend
            fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ image: imageData })
            })
            .then(response => response.json())
            .then(data => {
                predictionText.textContent = `Predicción: ${data.prediction}`;
            })
            .catch(error => console.error('Error:', error));
        }
        