def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


n = int(input("Digite um número inteiro positivo: "))

for i in range(2, n+1):
    if is_prime(i):
        print(i)