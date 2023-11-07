def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


numero = 5
resultado_fatorial = fatorial(numero)
print(f'O fatorial de {numero} é {resultado_fatorial}')

def somaNatural(n):
    if n == 0:
        return 0
    else:
        return n + somaNatural(n - 1)


numero_natural = 5
resultado_soma = somaNatural(numero_natural)
print(f'A soma dos números naturais até {numero_natural} é {resultado_soma}')

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


iteracoes_fibonacci = 8
resultado_fibonacci = fibonacci(iteracoes_fibonacci)
print(f'Sequência de Fibonacci para {iteracoes_fibonacci} iterações: {resultado_fibonacci}')
