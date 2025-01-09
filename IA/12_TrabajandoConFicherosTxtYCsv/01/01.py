def tabla_n():
    num = int(input("Introduce un número del 1 al 10\n"))
    tabla = []
    for i in range(1,11):
        tabla.append(num*i)
    
    strTabla=""
    for n,i in enumerate(tabla,start=1):
        strTabla+=f"{num} * {n} = {i}\n"

    with open(f"tabla_{num}.txt","w", encoding="utf-8") as f:
        f.write(strTabla)

tabla_n()

def mostrar_tabla_n():
    num = int(input("¿De qué número quieres saber la tabla de multiplicar?\n"))

    try: 
        with open(f"tabla_{num}.txt", "r", encoding="utf-8") as f:
            data = f.read()
        
        print(data)
    except Exception:
        print(f"No se ha encontrado el fichero tabla_{num}.txt")

mostrar_tabla_n()


def mostrar_linea_m_tabla_n():
    num = int(input("¿De qué número quieres saber la tabla de multiplicar?\n"))
    m = int(input("¿Qué fila desea conocer?\n"))
    try: 
        with open(f"tabla_{num}.txt", "r", encoding="utf-8") as f:
            data = f.readlines()
        
        print(f"\n{data[m]}")
    except Exception:
        print(f"No se ha encontrado el fichero tabla_{num}.txt")

mostrar_linea_m_tabla_n()