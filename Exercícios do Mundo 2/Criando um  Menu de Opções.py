from time import sleep
print('\n\033[33;1mMENU DE OPÇÕES\033[m\n')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

número = 0

while número != 5:
    print('''\nO que você gostaria de fazer com esses dois números?
    
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Saber qual é o maior
[ 4 ] Digitar novos números
[ 5 ] Sair do programa\n''')

    escolha = int(input('Digite o número da opção desejada: '))

    if escolha == 1:
        num4 = num1 + num2
        print(f'\nA soma entre {num1} + {num2} é igual a {num4}.\n')
        break
    
    elif escolha == 2:
        num5 = num1 * num2
        print(f'\nA multiplicação de {num1} x {num2} é igual a {num5}.\n')
        break
    
    elif escolha == 3:
        
        if num1 > num2:
            print('\nO primeiro número é o maior!\n')
            break
        elif num2 > num1:
            print('\nO segundo número é o maior!\n')
            break
    
    elif escolha == 4:
        print('\n\033[33;1mDigite os valores novamente\033[m')
        print(end='\n')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))

    elif escolha == 5:
        print('\nFinalizando...\n')
        sleep(0.7)
        print('Programa finalizado!\n')
        break
