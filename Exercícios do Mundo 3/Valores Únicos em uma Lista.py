números = list()

while True:
    print(end='\n')

    n = int(input('Digite um número: '))

    if n not in números:
        números.append(n)
        print('\nNovo valor adicionado!')

    else:
        print('\nNão digite valores iguais.')
    
    escolha = str(input('\nQuer continuar? [S/N] ')).upper().strip()
    if escolha in 'N':
        break

números.sort()
print(f'\nNúmeros digitados: {números}\n')
