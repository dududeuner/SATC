from random import randint

max = 10
tentativas = 0
num_sortead = randint(1, 100)

num = 0
while (tentativas < max) and (num_sortead != num):
    print(f'vc tem {max - tentativas}, chances')
    num = int(input('Adivinhe o numero sorteado (1 a 100): '))
    if num > num_sortead:
        print(f'numero sorteado eh menor q {num}')
    elif num < num_sortead:
        print(f'numero sorteado eh maior q {num}')
        
        if num == num_sortead:
          print(f'parabens vc acertou o numero sorteado'\
                f' em {tentativas} vezes')
        else:
          print(f'nao foi desta vez {num_sortead}')
