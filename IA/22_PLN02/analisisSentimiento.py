from textblob import TextBlob
from googletrans import Translator
import asyncio

# Traducimos para mejorar el reconocimiento de la polaridad y subjetividad
async def traducir(texto):
    async with Translator() as traslator:
        res = await traslator.translate(texto)
    return res.text


texto = "Me encanta aprender sobre inteligencia artificial, es fascinante."

# Esperamos el resultado de la traducción
texto_trad = asyncio.run(traducir(texto))

# Crear un objeto TextBlob con el texto traducido
blob = TextBlob(texto_trad)

# Analizar el sentimiento
sentimiento = blob.sentiment

# Imprimir los resultados
print(f"Polaridad: {sentimiento.polarity}")
print(f"Subjetividad: {sentimiento.subjectivity}")

