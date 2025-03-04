import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pares = [
    (r"hola|buenos días|buenas tardes", ["¡Hola! ¿Cómo puedo ayudarte hoy?"]),
    (r"adiós|hasta luego", ["¡Hasta luego! ¡Que tengas un buen día!"]),
    (r"¿cómo estás?", ["Estoy bien, gracias por preguntar. ¿Y tú?"]),
    (r"¿cuál es tu nombre?", ["Soy un chatbot creado en Python."]),
    (r"mi nombre es (.*)", ["Hola, %1. Encantado de conocerte."]),
    (r"(.*) (gracias|muchas gracias)", ["¡De nada!"]),
    (r"(.*)", ["Lo siento, no entendí eso. ¿Puedes reformular tu pregunta?"])
]

chatbot = Chat(pares, reflections)

def iniciar_chatbot():
    print("¡Hola! Soy un chatbot. Escribe 'adiós' para terminar la conversación.")
    while True:
        
        entrada = input("Tú: ")
        if entrada.lower() == "adiós":
            print("Chatbot: ¡Hasta luego!")
            break
        else:
            respuesta = chatbot.respond(entrada)
            print(f"Chatbot: {respuesta}")


iniciar_chatbot()