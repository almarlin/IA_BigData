import langdetect
import pyttsx3


def audioLibro(libro):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('voice', 'spanish')
    engine.save_to_file(libro, "elarboldelaciencia.mp3")
    engine.runAndWait()


def normalizarLibro(lineas):
    inicioLibro = (
        "                              PÍO BAROJA"
    )
    finLibro = (
        "                                  FIN"
    )

    # Se recoge el indice cuando las lineas coincidan con las de inicio y fin
    indexInicio = next((i for i, line in enumerate(lineas) if inicioLibro in line), 0)
    indexFin = next(
        (i for i, line in enumerate(lineas) if finLibro in line), len(lineas)
    )

    libro = " ".join(line.strip() for line in lineas[indexInicio:indexFin])
    return libro


with open("el_arbol_de_la_ciencia.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()

libro = normalizarLibro(lineas)
idioma = langdetect.detect(libro)
print("Generando audio del libro...")
audioLibro(libro)
print("Audio generado")

