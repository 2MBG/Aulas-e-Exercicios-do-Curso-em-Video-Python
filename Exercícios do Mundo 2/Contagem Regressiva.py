from time import sleep

print('\nOs fogos serão lançados em:\n')

for contagem in range(10, -1, -1):
    print(contagem)
    print(end='\n')
    sleep(1)

print('FELIZ ANO NOVO!\n')
