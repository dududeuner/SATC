def nome_salario(**kwargs):
    
    for chave, valor in kwargs.items():
        if valor is None:
            valor = 9000
        print(f'{chave}: {valor}')

    


nome_salario(nome = 'dudu', salario = None)