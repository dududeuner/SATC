num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

soma = num1

for i in range(num1 + 1, num2):
    print(i)
    soma += i

print("A soma dos numeros :", soma)