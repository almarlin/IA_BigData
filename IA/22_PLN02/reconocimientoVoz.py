import speech_recognition as sr

# Reconocimiento de voz desde el archivo WAV
r = sr.Recognizer()

with sr.AudioFile("ejemplo.wav") as source:
    audio_text = r.record(source)  # Grabar todo el archivo
    try:
        print(f"Texto: {r.recognize_google(audio_text, language='en')}")
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print(f"Error con el servicio de Google Speech Recognition; {e}")
