extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    print(end='\n')

    num = int(input('Digite um número de 0 a 20: '))

    print(end='\n')

    while num < 0 or num > 20:
        num = int(input('\033[31mOpção inválida.\033[m Digite um número de 0 a 20: '))
        print(end='\n')

    if num >= 0 and num <= 20:
        print(f'Você digitou o número {extenso[num]}.\n')

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

    while not continuar == 'S' and not continuar == 'N':
        continuar = str(input('\033[31mOpção inválida.\033[m Quer continuar? [S/N] ')).upper().strip()

    if continuar == 'N':
        print('\nPrograma encerrado.\n')
        break
