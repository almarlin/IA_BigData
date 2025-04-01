from cadena import Blockchain
from bloque import Bloque
import numpy as np


def generarBlockChain(bc):
    for i in range(1, 10):

        bc.agregar_bloque(
            emisor=str(np.random.randint(1, 5)),
            receptor=str(np.random.randint(1, 5)),
            mensaje=str(np.random.randint(100000, 999999)),
        )
        if np.random.randint(1, 5) == 1:
            bc.cadena[i].mensaje = "Modificado"


def modificarCadena(bc):
    valido = False
    while not valido:
        bloque = input("Introduce el id del bloque a modificar: ")
        try:
            id = int(bloque)
            if id in [block.id for block in bc.cadena]:
                valido = True
        except:
            print("Identificador inválido")

    bc.cadena[id].mensaje = input("Introduce el mensaje a modificar: \n")


def reparar(bc):
    for bloque in bc.cadena:
        hash_anterior = bloque.hash
        hash_actual = bloque.calcular_hash()

        if hash_actual != hash_anterior:
            print(f"Error detectado en el bloque [{bloque.id}].")
            print("Reparando la cadena.")
            bc.reparar(bloque.id)
            break
        hash_actual = bloque.hash


def __main__():
    bc = Blockchain()
    generarBlockChain(bc)
    bc.mostrar_transacciones()
    print(f"¿La cadena es válida? -> {bc.es_valida()}")
    if not bc.es_valida():
        reparar(bc)

    print(f"Se ha reparado la cadena. ¿Es esta válida? -> {bc.es_valida()}")
    bc.mostrar_transacciones()

    modificarCadena(bc)

    print(f"¿La cadena es válida? -> {bc.es_valida()}")
    bc.mostrar_transacciones()

    if not bc.es_valida():
        reparar(bc)

    print(f"Se ha reparado la cadena. ¿Es esta válida? -> {bc.es_valida()}")
    bc.mostrar_transacciones()

    bc.to_txt()


__main__()
