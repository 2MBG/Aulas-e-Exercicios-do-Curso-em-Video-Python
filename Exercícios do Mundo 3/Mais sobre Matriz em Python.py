matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
soma_coluna = 0
maior_valor = 0

print(end='\n')

for linha in range(0, 3): # Três para as colunas
    for coluna in range(0, 3):
        matriz [linha][coluna] = int(input(f'Digite um valor para linha {linha} coluna {coluna}: '))

print(end='\n')
print('=' * 38)
print(end='\n')

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha] [coluna]:^5}]', end='')
        
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz [linha][coluna]

    print()

print(end='\n')
print('=' * 38)
print(end='\n')

print(f'A soma dos valores pares é igual a {soma_par}.')

for linha in range(0, 3):
    soma_coluna += matriz[linha][2] # O valor da coluna já está fixado sendo assim somente o valor da linha irá variar.
print(f'A soma dos valores da 3ª coluna é igual a {soma_coluna}.')

for coluna in range(0, 3):
    if coluna == 0: # O primeiro elemento é sempre o maior
        maior_valor = matriz[1][coluna]
    
    elif matriz[1][coluna] > maior_valor: # Caso não seja, o elif faz uma compração com o maior valor
        maior_valor =matriz[1][coluna]
print(f'O maior valor da 2ª coluna é o {maior_valor}.\n')
