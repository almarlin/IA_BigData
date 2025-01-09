def fib(num):

    fib = list([0,1])

    for i in range(2,num):
        sig = fib[i-1] + fib[i-2]
        fib.append(sig)
    return fib

n = int(input("Introduce un número: "))

print(f"La serie de Fibonacci hasta {n} elementos es: {fib(n)}")