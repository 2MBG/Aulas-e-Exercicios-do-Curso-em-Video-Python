num1 = float(input('\nQuantos metros de altura tem a parede em questão? '))
num2 = float(input('\nE quantos metros de largura? '))
num3 = num1 * num2
num4 = num3 / 2

print(f'\nSua parede possui uma área de {num3:.1f}m².' 
f'Serão necessários {num4:.1f} litros de tinta para pintá-la.\n')
