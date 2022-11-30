valores = []

while True:
    print(end='\n')
    
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('\nQuer continuar: [S/N] ')).upper()
    
    while not resposta == 'S' and not resposta == 'N':
        resposta = str(input('\nOpção inválida. Quer continuar: [S/N] ')).upper()

    if resposta in 'N':
        break

print(f'\nTotal de valores digitados: {len(valores)}')
valores.sort(reverse = True)
print(f'Os valores em ordem decrescente são {valores}')

if 5 in valores:
    print('O valor 5 faz parte da lista.\n')

else:
    print('O valor 5 não faz parte da lista.\n')
