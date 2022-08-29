cor = str(input('\nDigite o nome de uma cor: ')).upper()

if cor == 'AZUL':
    print('\n\033[34;1mA cor mais bonita de todas!\033[m\n')

elif cor == 'VERDE' or cor == 'PRETO':
    print('\nEssa cor combina com quase tudo!\n')

elif cor == 'CINZA':
    print('\nG59\n')

else:
    print('\nVocê tem bom gosto!\n')
