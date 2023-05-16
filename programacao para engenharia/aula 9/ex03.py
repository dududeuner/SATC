notas = []
alunos_aprovados = 0


for i in range(10):
    notas_aluno = []
    for j in range(4):
        nota = float(input(f"Informe a {j+1}ª nota do aluno {i+1}: "))
        notas_aluno.append(nota)
    

    media = sum(notas_aluno) / len(notas_aluno)
    notas.append(media)
    
    
    if media >= 7:
        alunos_aprovados += 1


print(f"Numero de alunos aprovados: {alunos_aprovados}")