print(end='\n')
print('=' * 50)
print('\033[33mDIGITE UM NÚMERO PARA SABER SE ELE É ÍMPAR OU PAR\033[m')
print('=' * 50)
print(end='\n')

número = int(input('Digite um número inteiro: '))

if número % 2 == 0:
    print("\n\033[36;1mPar\033[m\n")

else:
    print("\n\033[31;1mÍmpar\033[m\n")
