premio = float(input('Valor do PREMIO:'))
ganhadores = int(input('Total de GANHADORES:'))

print (f'O PREMIO DE R$ {premio: ,.2f}, COM {ganhadores} GANHADORES, RECEBERAM R${premio/ganhadores:,.2f}')