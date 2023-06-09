funcionarios = {1: "João", 2: "Maria", 3: "Pedro", 4: "Ana"}

print("Funcionários:")

for chave, valor in funcionarios.items():
 print(f"{chave}: {valor}")

 
demitido = int(input("Digite o número do funcionário a demitir: "))
del funcionarios[demitido]

print("Funcionários restantes:")
for chave, valor in funcionarios.items():
 print(f"{chave}: {valor}") 
