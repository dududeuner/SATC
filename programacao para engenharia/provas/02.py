altura = float(input("Digite a altura em metros: "))
peso = float(input("Digite o peso em kg: "))
sexo = input("Digite o sexo, M para masculino, F para feminino: ")

if sexo == 'M' or 'm':
    peso_ideal = (72.7 * altura) - 58
    if peso < peso_ideal:
        situacao = "abaixo do peso ideal"
    elif peso > peso_ideal:
        situacao = "acima do peso ideal"
    else:
        situacao = "no peso ideal"
elif sexo == 'F' or 'f':
    peso_ideal = (62.1 * altura) - 44.7
    if peso < peso_ideal:
        situacao = "abaixo do peso ideal"
    elif peso > peso_ideal:
        situacao = "acima do peso ideal"
    else:
        situacao = "no peso ideal"
else:
    print("Sexo inválido. Digite M para masculino ou F para feminino.")
    exit()

print(f"O peso ideal para a altura {altura}m é {peso_ideal:.2f}kg.")
print(f"Você está {situacao}.")