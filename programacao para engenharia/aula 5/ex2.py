num = 0
soma = 0
n = 0
maior = 0
menor = 0
while num != -1:
    num = int(input('Digite um numero: '))
    if num > 0:
        soma = soma + num
    n = n + 1
    if num > maior:
        maior = num
    if num < menor and num != -1:
        menor = num
print('Soma de todos : ',soma)
print('media : ', soma /n)
print('Numero de numeros : ',n)
print('Maior numero : ',maior)
print('Menor numero : ',menor)
