num = list()
pares = list()
ímpares = list()

while True:
    print(end='\n')
    
    num.append(int(input('\033[33mDigite um valor:\033[m ')))
    resp = str(input('\nQuer continuar? [S/N] ')).upper()

    while not resp == 'S' and not resp == 'N':
        resp = str(input('\n\033[31mOpção inválida.\033[m Quer continuar? [S/N] ')).upper()

    if resp in 'N':
        break

for índice, valor in enumerate(num):
    if valor % 2 == 0:
        pares.append(valor)
    
    elif valor % 2 == 1:
        ímpares.append(valor)

print(f'\nNúmeros digitados: {num}')
print(f'Números pares digitados: {pares}')
print(f'Número ímpares digitados: {ímpares}\n')
