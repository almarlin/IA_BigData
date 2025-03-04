import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):

    # Tokenizar el texto usando nltk
    tokens = nltk.word_tokenize(text.lower())

    # Eliminar puntuación y palabras vacías
    stopwords = nltk.corpus.stopwords.words('spanish')
    # Se comprueba que las palabras no esten en la lista de stopwords y sean alfabeticas
    tokens = [word for word in tokens if word.isalpha() and word not in stopwords]
    return ' '.join(tokens)

def get_response(user_input):

    # Preprocesar la entrada del usuario
    user_input_processed = preprocess_text(user_input)
    
    # Si la pregunta es igual, se devuelve la respuesta
    if user_input in defined_entries:
        return defined_entries[user_input]
    
    # Convertir la entrada del usuario en un vector TF-IDF
    user_input_vector = vectorizer.transform([user_input_processed])
    
    # Calcular la similitud del coseno entre la entrada las respuestas
    cosine_similarities = cosine_similarity(user_input_vector, tfidf_matrix)
    
    # Encontrar el índice de la respuesta más similar
    most_similar_index = cosine_similarities.argmax()
    
    return responses[most_similar_index]

# Definir las entradas y respuestas específicas
defined_entries = {
    "¿Como te llamas?": "Soy un chatbot sin nombre, pero puedes llamarme como quieras.",
    "¿Que hora es?": "Lo siento, no tengo acceso a la hora exacta, pero puedes consultar la hora en tu dispositivo.",
    "¿Que es NLTK?": "NLTK (Natural Language Toolkit) es una librería para el procesamiento de lenguaje natural en Python.",
    "¿Quien eres?": "Soy un chatbot diseñado para ayudarte a obtener información o mantener una conversación.",
    "¿Que es Python?": "Python es un lenguaje de programación popular y fácil de aprender.",
    "¿Como puedo usar un chatbot?": "Solo necesitas escribir preguntas o frases y yo intentaré responder lo mejor posible.",
    "¿Dónde vives?": "Soy un programa, así que no tengo una ubicación física, pero estoy aquí para ayudarte.",
    "¿Que es el machine learning?": "El machine learning (aprendizaje automático) es un campo de la inteligencia artificial que permite a las máquinas aprender de datos y hacer predicciones o decisiones.",
    "¿Cuantos años tienes?": "No tengo edad, soy un programa creado para ayudarte con preguntas.",
    "Adios": "¡Adiós! Espero haberte ayudado, vuelve cuando necesites más ayuda."
}
responses = list(defined_entries.values())

# Preprocesar las respuestas predefinidas
processed_responses = [preprocess_text(response) for response in responses]

# Crear un vectorizador TF-IDF
vectorizer = TfidfVectorizer()

# Preprocesar las respuestas predefinidas y ajustarlas al modelo
tfidf_matrix = vectorizer.fit_transform(processed_responses)

# Chat
print("¡Hola! Soy un chatbot. Escribe 'salir' para terminar la conversación.")
while True:
    user_input = input("Tú: ")
    if user_input.lower() == 'salir':
        print("¡Adiós!")
        break
    response = get_response(user_input)
    print("Chatbot: " + response)
