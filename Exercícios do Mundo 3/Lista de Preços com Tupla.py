listagem = ('Kit 4 travesseiros', 227.90, 'Suporte p/ Headset', 50.56, 'Suporte articulado p/ monitor', 235.90,
            'Teclado Mecânico', 585, 'Case para HD', 45.99, 'Anker Life Q30', 546.55, 'Kontrol Freek', 89.90,
            'Introdução à Linguagem SQL', 40.14, 'Mesa Gamer', 289.99, 'Código Limpo', 71.99, 'Mouse G203', 129.90,
            'Engenharia de Software', 193.91, 'Fundamentos Mat. p/ Ciência da Compt.', 317.87, 'Python Fluente', 98.84,
            'Python para Análise de Dados', 89.85, 'TDD com Python', 93.74, 'Algoritmos: Lógica para Desenv. de Programas', 74.01)

print(end='\n')
print('=' * 58)
print(f'\033[32;1m{"CARRINHO DE COMPRAS":^58}\033[m')
print('=' * 58)
print(end='\n')

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'\033[34;4;7;1m-{listagem[pos]: <47}\033[m', end='')
    
    else:
        print(f'\033[36;7;4;1mR${listagem[pos]:>7.2f} \033[m')

print(end='\n')
