print("Praticando com o Python...")
print("************************************************")
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("************************************************")
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("************************************************")

opcao = int(input("Qual grandeza deseja calcular? "))

if opcao == 1:
    R = float(input("Informe o valor da resistência em Ohm: "))
    i = float(input("Informe o valor da corrente em Ampére: "))
    U = R*i
    print("A tensão é de", U, "V.")
elif opcao == 2:
    U = float(input("Informe o valor da tensão em Volt: "))
    i = float(input("Informe o valor da corrente em Ampére: "))
    R = U/i
    print("A resistência é de", R, "Ohm.")
elif opcao == 3:
    U = float(input("Informe o valor da tensão em Volt: "))
    R = float(input("Informe o valor da resistência em Ohm: "))
    i = U/R
    print("A corrente é de", i, "Ampére.")
else:
    print("Opção inválida.")