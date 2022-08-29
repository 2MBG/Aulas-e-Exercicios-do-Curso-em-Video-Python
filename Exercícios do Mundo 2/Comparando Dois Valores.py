print('\n\033[33mDigite dois números inteiros para compará-los:\033[m')

num1 = int(input('\nPrimeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('\nO primeiro número é o maior!\n')

elif num2 > num1:
    print('\nO segundo número é o maior!\n')

elif num1 == num2:
    print('\nOs dois números são iguais!\n')
