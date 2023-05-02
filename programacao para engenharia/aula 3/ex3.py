import math

nome = str(input('digite seu nome :  '))
imoveis = int(input('digite a quantidade de imoveis vendidos :  '))
vendas = int(input('digite o valor total em vendas :  '))

comissao = 200

salario = 1500

porcentagem = vendas * 5 / 100

sum = 0

for imoveis in range(imoveis):
    sum = sum + comissao


print(sum + salario + porcentagem)