numeros = []


for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)


print("Números pares:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)