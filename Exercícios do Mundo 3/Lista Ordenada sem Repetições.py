lista = []

for c in range(0, 5):
    print(end='\n')
    
    n = int(input('\033[33mDigite um valor:\033[m '))

    if c == 0 or n > lista[-1]: # Adiciona o primeiro e o último
        lista.append(n)
        print('\nAdicionado ao final da lista')

    else: # Adiciona nas outras posições
        pos = 0
        while pos < len(lista):
            
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'\nAdicionado na posição {pos} da lista.')
                break
            pos += 1

print(f'\nValores ordenados: {lista}\n')
