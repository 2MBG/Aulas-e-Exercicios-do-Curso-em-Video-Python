from random import randint
from time import sleep

lista = []
jogos = []

print(end='\n')
print('=' * 30)
print(f'\033[33;1m{"JOGANDO NA MEGA SENA":^30}\033[m')
# print('=' * 30, f'\033[33;1m{"JOGANDO NA MEGA SENA":^30}\033[m', '=' * 30)
print('=' * 30)
print(end='\n')

quantidade = int(input('Quantos jogos você quer jogar? '))
total_de_jogos = 1

while total_de_jogos <= quantidade:
    contador = 0
    while True:
        num = randint(1, 60)
        
        if num not in lista:
            lista.append(num)
            contador += 1
        
        if contador >= 6:
            break
    
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total_de_jogos += 1

print(end='\n')
print('=' * 30)
print(f'\033[32;1m{f"SORTEANDO {quantidade} JOGOS":^30}\033[m')
# print('=' * 30, f'\033[32;1m{f"SORTEANDO {quantidade} JOGOS":^30}\033[m', '=' * 30)
print('=' * 30)
print(end='\n')

for índice, lista in enumerate(jogos):
    sleep(1)
    print(f'Jogo {índice + 1}: {lista}')

print('\nBOA SORTE!\n')
