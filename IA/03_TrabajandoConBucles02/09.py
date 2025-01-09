num = int(input("Indica cuantos número de la serie de Fibonacci quieres conocer: "))

fib = list([0,1])

for i in range(2,num):
    sig = fib[i-1] + fib[i-2]
    fib.append(sig)

print("Serie de Fibonacci: ")
print(fib)