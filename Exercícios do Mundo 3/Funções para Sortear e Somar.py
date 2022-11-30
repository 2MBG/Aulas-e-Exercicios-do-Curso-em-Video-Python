from random import randint
from time import sleep

def sorteia(lista):
    print(end='\n')
    print('Sorteando 5 valores da lista: ', end='')
    
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'\033[33m{n}\033[m ', end='', flush=True)
        sleep(0.5)
    print('- Pronto!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nA soma dos valores pares de \033[33m{lista}\033[m é igual a \033[32;1m{soma}\033[m.\n')


números = list()
sorteia(números)
somaPar(números)
