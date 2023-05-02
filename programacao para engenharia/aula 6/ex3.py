while True:
    
    print("Escolha uma opção:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    
    opcao = int(input("Opção: "))

    
    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print("Resultado: ", resultado)
    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print("Resultado: ", resultado)
    elif opcao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print("Resultado: ", resultado)
    elif opcao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 == 0:
            print("Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print("Resultado: ", resultado)
    elif opcao == 5:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
    
    
    print()