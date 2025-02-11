import spacy

# Separar un texto en palabras y analizar su estructura gramatical

# Hay que instalar el paquete a utilizar con pip. Este es el español small
pln = spacy.load("es_core_news_sm")

texto = "El procesamiento del lenguaje natural es una rama de la inteligencia artificial."

doc = pln(texto)

# Mostramos el texto, su origen morfologico y su tipo (pronombre, verbo, determinante, etc)
for token in doc:
    print(f"Texto: {token.text}, Lemma: {token.lemma_}, Tipo: {token.pos_}")
