num = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))
op = input("Ingresa un operador ('+' , '-' , '/' , '*'): ")

tot = 0

match op:
    case "+":
        tot = num + num2
        print(f"Total: {tot}")
    case "-":
        tot = num - num2
        print(f"Total: {tot}")
    case "/":
        tot = num / num2
        print(f"Total: {tot}")
    case "*":
        tot = num * num2
        print(f"Total: {tot}")
    case _:
        print("Operación no encontrada")
