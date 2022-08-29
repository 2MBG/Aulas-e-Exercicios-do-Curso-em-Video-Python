from math import sqrt

cateto = float(input('\n\033[37;1mDigite o valor do cateto: \033[m'))
cateto_adjacente = float(input('\n\033[37;1mDigite o valor do cateto adjacente: \033[m'))
hipotenusa = (cateto ** 2 + cateto_adjacente ** 2)
hipotenusa2 = sqrt(hipotenusa)

print(f'\n\33[37;1mO valor da hipotenusa é:\033[m {hipotenusa2:.2f}!\n')

# from math import hypot
# cateto = float(input('\nDigite o valor do cateto: '))
# cateto_adjacente = float(input('\nDigite o valor do cateto adjacente: '))
# hipotenusa = hypot(cateto, cateto_adjacente)
# print(f'\nO valor da hipotenusa é: {hipotenusa:.2f}!\n')
