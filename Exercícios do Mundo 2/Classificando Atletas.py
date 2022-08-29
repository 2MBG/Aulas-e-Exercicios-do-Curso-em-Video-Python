idade = int(input('\nQuantos anos você tem? '))

if idade <= 9:
    print('\nVocê é um nadador Mirim!\n')

elif idade <= 14:
    print('\nVocê é um nadador Infantil!\n')

elif idade <= 19:
    print('\nVocê é um nadador Junior!\n')

elif idade <= 25:
    print('\nVocê é um nadador Sênior!\n')

elif idade > 25:
    print('\nVocê é um nadador Master!\n')
