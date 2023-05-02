num1 = float(input('digite a sua velocidade : '))
num2 = float(input('digite a velocidade maxima da avenida : '))

if((num1 > num2 + 1) and (num1 < num2 + 11)):

    print('Multa de 85,13 Reais, leve 3 pontos na carteira')

elif((num1 > num2 + 11) and (num1 < num2 + 31)):

    print('Multa de 127,69 Reais, media 5 pontos na carteira')

elif((num1 >= num2 + 31)):

    print('Multa de 573,62 Reais, gravissima 7 pontos na carteira')

else:
    print('Vel. Normal')        
