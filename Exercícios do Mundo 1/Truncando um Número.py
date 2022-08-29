# TRUNCAR remove a parte fracionária do número. 

from math import trunc

num1 = float(input('\nDigite um número decimal: '))
decimal = trunc(num1)

print(f'\nA parte inteira de {num1} é igual a: {trunc(decimal)}.\n')
