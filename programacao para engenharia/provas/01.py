meses = {
    '01': 'janeiro', '02': 'fevereiro', '03': 'março', '04': 'abril',
    '05': 'maio', '06': 'junho', '07': 'julho', '08': 'agosto',
    '09': 'setembro', '10': 'outubro', '11': 'novembro', '12': 'dezembro'
}
data_valida = False

data = input("Digite uma data no formato DD/MM/AAAA: ")

if len(data) == 10 and data[2] == data[5] == '/':
    dia = data[:2]
    mes = data[3:5]
    ano = data[6:]
    
    if dia.isdigit() and mes.isdigit() and ano.isdigit():
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
       
        if 1 <= dia <= 31 and 1 <= mes <= 12:
            data_valida = True
if data_valida:
    mes_por_extenso = meses[mes]
    data_formatada = f"{dia} de {mes_por_extenso} de {ano}"
    print(data_formatada)
else:
    print("Data inválida. Digite uma data no formato DD/MM/AAAA.")
