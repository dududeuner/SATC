nome_ginasta = input("Digite o nome: ")

notas = []

for i in range(7):
    nota = float(input("Nota: "))
    notas.append(nota)

melhor_nota = max(notas)
pior_nota = min(notas)

media = sum(notas) / len(notas)

print("\nResultado final:")
print(f"Atleta: {nome_ginasta}")
print("Notas:")

for nota in notas:
    print(f"Nota: {nota}")

print(f"Atleta: {nome_ginasta}")
print(f"Melhor nota: {melhor_nota}")
print(f"Pior nota: {pior_nota}")
print(f"Média: {media:.2f}")