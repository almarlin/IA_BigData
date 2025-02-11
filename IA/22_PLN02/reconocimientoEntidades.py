import spacy

# dentificar nombres de personas, lugares y organizaciones en un texto.

pln = spacy.load("es_core_news_sm")

texto = "El fundador de Tesla, Elon Musk, ha invertido en inteligencia artificial."

doc = pln(texto)

for entity in doc.ents:
    print(f"Nombre: {entity.text}, ID: {entity.label_}, Raíz: {entity.root}")