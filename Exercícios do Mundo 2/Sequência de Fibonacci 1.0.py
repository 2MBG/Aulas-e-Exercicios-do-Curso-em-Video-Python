# Fn = Fn - 1 + Fn - 2 Fórmula da Sequência

# 0 → 1 → 1 → 2 → 3 → 5 → 8

'''Exemplo:
3 + 2 = 5
5 + 3 = 8
8 + 5 = 13
13 + 8 = 21
21 + 13 = 34
34 + 21 = 55
55 + 34 = 89   
'''

print(end='\n')
print('-' * 22)
print('\033[34;1mSequência de Fibonacci\033[m')
print('-' * 22)
print(end='\n')

número = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1

print(f'\n{termo1} → {termo2}', end='')

contador = 3 # É três pois o 0 e 1 já foram apresentados.

while contador <= número:
    
    termo3 = termo1 + termo2
    termo1 = termo2
    print(f' → {termo3}', end='')
    termo2 = termo3
    contador = contador + 1

print(' → FIM DA SEQUÊNCIA!\n')
