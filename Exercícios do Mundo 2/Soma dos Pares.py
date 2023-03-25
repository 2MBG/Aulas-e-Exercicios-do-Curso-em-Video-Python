print('\n\033[33;1mSomando Números Pares\033[m\n')

soma = 0
contator = 0

for contagem in range(1, 7):
    
    num = int(input(f'Digite o {contagem}° valor: '))
    
    if num % 2 == 0:
        soma += num
        contator += 1
    
print(f'\nSomando {contator} valor(es) \033[37;1mPAR(ES)\033[m, teremos: {soma}.\n')
