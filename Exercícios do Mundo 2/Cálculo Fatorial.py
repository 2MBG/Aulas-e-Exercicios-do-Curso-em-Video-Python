from math import factorial

número = int(input('\nDigite um número para cálcular seu fatorial: '))
fatorial = factorial(número)

print(f'\nO fatorial de {número}! é {fatorial}.\n')


# Com o while
'''
número = int(input('\nDigite um número para cálcular seu fatorial: '))
contador = n
fatorial = 1
print(f'Calculando {número}! = ', end='')

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')'''
