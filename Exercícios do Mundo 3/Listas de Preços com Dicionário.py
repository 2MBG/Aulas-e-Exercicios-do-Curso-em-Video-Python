print(end='\n')
print('=' * 35)
print(f'\033[32;1m{"COMPRAS":^35}\033[m')
print('=' * 35)
print(end='\n')

compras = {'Leite': 4.00, 'café': 5.00, 'Açúcar': 4.30, 
           'Frutas': 3.00, 'Pão': 0.50, 'Bolacha': 1.50, 'Leite Condesado': 3.50,
           'Toddy': 5.00, 'Suco': 1.00, 'Energético': 3.40, 'Pudim': 9.00, 'Legumes': 4.50
          }

for chaves,valores in compras.items():
    print(f'\033[34;4;7;1m{chaves:<15} - R${valores:<15.2f}\033[m')

print(end='\n')
