número = 0
soma = 0

print(end='\n')

while True: # Loop infinito
    número = int(input('Digite um número (999 para encerrar): '))

    if número == 999:
        break # Interrompe um laço de repetição
    
    soma = soma + número

print(f'\nA soma dos números digitados é igual a {soma}.\n')
