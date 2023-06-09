def media():
    nota = float(input('digite a primeira nota : '))
    nota2 = float(input('digite a segunda nota : '))
    nota3 = float(input('digite a terceira nota : '))

    soma = nota + nota2 + nota3
    media_notas = soma / 3

    
    if media_notas >= 6:
        print(f'aluno aprovado com {media_notas:.2f}')

    elif media_notas <= 6 and media_notas >= 4:
         print(f'verificação suplementar')

    elif media_notas < 4:
         print(f'aluno reprovado com {media_notas:.2f} pontos')


    
media()