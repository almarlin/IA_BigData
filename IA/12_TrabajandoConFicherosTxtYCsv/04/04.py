import csv


def list_dict_alumno(path):

    with open(path, "r", encoding="utf-8") as f:
        data = csv.reader(f, delimiter=";")
        notas = list()

        for i, d in enumerate(data):
            if i != 0:
                notas.append(
                    {
                        "Apellidos": d[0],
                        "Nombre": d[1],
                        "Asistencia": d[2],
                        "Parcial1": (
                            float(d[3].replace(",", "."))
                            if d[3].replace(",", ".")
                            else 0
                        ),
                        "Parcial2": (
                            float(d[4].replace(",", "."))
                            if d[4].replace(",", ".")
                            else 0
                        ),
                        "Ordinario1": (
                            float(d[5].replace(",", "."))
                            if d[5].replace(",", ".")
                            else 0
                        ),
                        "Ordinario2": (
                            float(d[6].replace(",", "."))
                            if d[6].replace(",", ".")
                            else 0
                        ),
                        "Practicas": (
                            float(d[7].replace(",", "."))
                            if d[7].replace(",", ".")
                            else 0
                        ),
                        "OrdinarioPracticas": (
                            float(d[8].replace(",", "."))
                            if d[8].replace(",", ".")
                            else 0
                        ),
                    }
                )

    return notas


def notaFinal(notas):
    for nota in notas:
        nota["Nota Final"] = (
            nota["Parcial1"] * 0.3 + nota["Parcial2"] * 0.3 + nota["Practicas"] * 0.4
        )

    return notas


def aprobadosYsuspensos(notasFinales):
    aprobados = []
    suspensos = []
    for nota in notasFinales:
        if nota["Nota Final"] >= 5:
            aprobados.append(nota)
        else:
            suspensos.append(nota)

    return aprobados,suspensos

notas = list_dict_alumno("calificaciones.csv")
print(notas)
notasFinales = notaFinal(notas)
print(notasFinales)

aprobados,suspensos = aprobadosYsuspensos(notasFinales)
print(aprobados)
print(suspensos)