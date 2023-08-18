class Aluno:
    def __init__(self, nome, idade, nota1, nota2):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2
    
    def calcula_media(self):
        return (self.nota1 + self.nota2) / 2
    
    def mostra_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Nota 1:", self.nota1)
        print("Nota 2:", self.nota2)
    
    def resultado(self):
        media = self.calcula_media()
        if media >= 6.0:
            return "Aprovado"
        else:
            return "Reprovado"

aluno1 = Aluno("Eduardo", 18, 7.5, 8.0)
aluno2 = Aluno("teste123", 20, 5.0, 6.5)

aluno1.mostra_dados()
print("Média:", aluno1.calcula_media())
print("Resultado:", aluno1.resultado())
print()

aluno2.mostra_dados()
print("Média:", aluno2.calcula_media())
print("Resultado:", aluno2.resultado())