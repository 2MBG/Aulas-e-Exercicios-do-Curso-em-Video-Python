# from <nome do módulo> import <funcionalidade>
# import: Importa todas as funcionalidades do módulo
# raiz = math.sqrt(num1)

from math import sqrt

num1 = int(input('\nDigite um número: '))
raiz = sqrt(num1) 

print(f'\nA raiz quadrada de {num1} é igual a {raiz:.1f}\n')
