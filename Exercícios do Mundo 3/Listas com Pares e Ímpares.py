print('\nPARES E ÍMPARES EM ORDEM CRESCENTE')

lista = [[], []] # Lista 0 e 1, respectivamente.

print(end='\n')

for c in range(1, 8):
    num = int(input((f'Digite um número ({c}/7): ')))
    
    if num % 2 == 0:
        lista[0].append(num)  # Números pares
    
    elif num % 2 == 1:
        lista[1].append(num)  # Números ímpares

print(f'\nNúmeros pares em ordem crescente: {sorted(lista[0])}')
print(f'Números ímpares em ordem crescente: {sorted(lista[1])}\n')
