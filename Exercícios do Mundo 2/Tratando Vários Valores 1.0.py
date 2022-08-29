número = 0
contador = 0
soma = 0

print('\nDigite 999 para encerrar.')

número = int(input('\nDigite um número: '))

while número != 999:
    soma = soma + número
    contador = contador + 1
    número = int(input('Digite um número: '))

print(f'\nA soma dos {contador} números digitados é igual a {soma}.\n')
