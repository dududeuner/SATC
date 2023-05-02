num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

numeros_positivos = 0
numeros_negativos = 0
if num1 >= 0:
    numeros_positivos += 1
else:
    numeros_negativos += 1

if num2 >= 0:
    numeros_positivos += 1
else:
    numeros_negativos += 1

if num3 >= 0:
    numeros_positivos += 1
else:
    numeros_negativos += 1

if num4 >= 0:
    numeros_positivos += 1
else:
    numeros_negativos += 1

percentual_positivos = (numeros_positivos / 4) * 100
percentual_negativos = (numeros_negativos / 4) * 100

media = (num1 + num2 + num3 + num4) / 4

print("A média aritmética dos números é:", media)
print("A quantidade de valores positivos é:", numeros_positivos)
print("A quantidade de valores negativos é:", numeros_negativos)
print("O percentual de valores positivos é:", percentual_positivos, "%")
print("O percentual de valores negativos é:", percentual_negativos, "%")