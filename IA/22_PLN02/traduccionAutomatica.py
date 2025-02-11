from googletrans import Translator
import asyncio


# Para traducir con googletrans es necesario una funcion asíncrona ya que se conecta a google
async def traducir(texto,dest="en"):
    async with Translator() as traslator:
        res = await traslator.translate(texto,dest=dest)
    return res.text


texto = (
    "El aprendizaje profundo está revolucionando el procesamiento del lenguaje natural."
)

dest = input("Introduce el codigo de idioma para traducir [fr,de,it,ja,ko,zh,ar]:\n")
# Esperamos el resultado de la traducción
texto_trad = asyncio.run(traducir(texto,dest))

print(f"Orgiginal: {texto}")
print(f"Traducido: {texto_trad}")
