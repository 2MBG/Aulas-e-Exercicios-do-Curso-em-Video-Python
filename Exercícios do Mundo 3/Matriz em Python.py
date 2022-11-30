matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(end='\n')

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz [linha][coluna] = int(input(f'Digite um valor para linha {linha} coluna {coluna}: '))

print(end='\n')
print('=' * 38)
print(end='\n')

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha] [coluna]:^5}]', end='')
    print()

print(end='\n')
print('=' * 38)
print(end='\n')
