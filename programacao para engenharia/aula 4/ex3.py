num1 = float(input('digite o salario : '))

if(num1 >= 1000):
    num1 += num1 * 10 / 100
    print(num1)
else:
        num1 += num1 * 5 / 100
        print(num1)