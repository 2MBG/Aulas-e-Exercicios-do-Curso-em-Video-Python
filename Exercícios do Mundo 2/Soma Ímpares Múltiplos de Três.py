print('\n\033[33;1mSomando todos os números ímpares que são múltiplos de 3 entre 1 e 500:\033[m')

soma = 0
contador = 0

for contagem in range(1, 501, 2):
    
    if contagem % 3 == 0:
        contador = contador + 1
        soma = soma + contagem
        
        #contador += 1
        #soma += contagem

print(f'\n\033[37;1mCom um total de \033[32;1m{contador}\033[m \033[37;1mvalores a soma é igual a\033[m \033[32;1m{soma}\033[m.\n')
