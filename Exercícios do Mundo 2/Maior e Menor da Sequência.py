print('\nVERIFICANDO PESOS\n')

maior_peso = 0
menor_peso = 0

for pessoa in range(1,6):
    peso = float(input(f'Peso da {pessoa}ª pessoa: '))
    
    if pessoa == 1: # Se for a 1ª pessoa ela vai ser a mais pesada e a mais leve.
        maior_peso = peso
        menor_peso = peso

    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso

print(f'\nO maior peso lido foi {maior_peso:.1f}Kg!')
print(f'O menor peso lido foi {menor_peso:.1f}Kg!\n')
