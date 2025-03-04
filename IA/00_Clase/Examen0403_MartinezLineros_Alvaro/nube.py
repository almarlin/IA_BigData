import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

# Se abre el fichero y se vuelca el texto
with open("el_quijote.txt","r",encoding="utf-8") as f:
    data = f.read()

# Se tokeniza
nltk.download('punkt')
tokens = word_tokenize(data)

# Eliminar puntuación y convertir todo a minusculas
tokens = [word.lower() for word in tokens if word.isalpha()]
# Se calcula la distribución de palabras.
fdist = FreqDist(tokens)
# Mostrar las 10 palabras más frecuentes
print(fdist.most_common(10))

# Se unen los tokens para generar la nube
text = " ".join(tokens)
# Se genera la nube
wordcloud = WordCloud().generate(text=text)

plt.imshow(wordcloud,interpolation="bilinear")
plt.axis("off")
plt.savefig("nube.png")
plt.show()
