senha_correta = "987654" 

while True: 
    senha = input("Digite a senha de seis dígitos: ")

    if senha == senha_correta:
        print("Cofre aberto!")
        break 
    else:
        print("Senha incorreta. Tente novamente.")