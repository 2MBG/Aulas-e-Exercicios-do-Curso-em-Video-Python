from time import sleep

def maior(* num):
    cont = maior = 0
    print('-' * 33)
    print('\033[33mAnalisando os valores passados... \033[m')
    
    for valor in num:
        sleep(0.5)
        print(f'{valor} ', end='', flush=True)

        if cont == 0:
            maior = valor
        
        else:
            if valor > maior:
                maior == valor
        cont += 1
    
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.\n')


maior(9, 5, 4, 7, 2, 1)
maior(1, 2, 6)
maior(6, 2, 4, 9, 22, 1)
maior(2)
maior()
