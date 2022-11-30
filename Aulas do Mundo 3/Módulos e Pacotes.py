from úteis import números

num = int(input('\nDigite um número: '))
fat = números.fatorial(num)

print(f'\nO fatorial de {num} é {fat}')
print(f'O dobro de {num} é {números.dobro(num)}') # úteis. para fazê-lo funcionar
print(f'O triplo de {num} é {números.triplo(num)}\n')
