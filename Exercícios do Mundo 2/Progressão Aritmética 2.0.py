print('\n\033[33;1mGERADOR DE PA\033[m')

primeiro = int(input('\nPrimeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
contador = 1

print(end='\n')

while contador <= 10: # Vai contar até 10
    print(f'{termo} → ', end='')
    termo = termo + razão
    contador = contador + 1

print('FIM\n')
