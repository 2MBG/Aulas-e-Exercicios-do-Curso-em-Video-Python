from random import randint
from time import sleep
from operator import itemgetter

print('\nValores sorteados:\n')

jogadores = {
            '1° Jogador': randint(1, 6),
            '2° Jogador': randint(1, 6),
            '3° Jogador': randint(1, 6),
            '4° Jogador': randint(1, 6)
}
ranking = []

for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)

ranking = sorted(jogadores.items(), key = itemgetter(1), reverse=True) # Pega os números que estão no índice 1

print(end='\n')
print('=' * 30)
print(f'{"RANKING":^30}')
print('=' * 30)
print(end='\n')

for i, v in enumerate(ranking):
    print(f'{i +1}° lugar: {v[0]} com {v[1]}.')

print(end='\n')
