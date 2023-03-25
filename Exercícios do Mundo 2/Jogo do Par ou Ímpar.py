from random import randint
from time import  sleep

vitórias = 0
escolha = ''

print('\n\033[33;1mPAR OU ÍMPAR\033[m\n')

while True:
    jogador = int(input('Digite um número: '))

    escolha = str(input('\nVocê quer par ou ímpar? [P/I] ')).upper().strip()[0]

    computador = randint(0,10)

    total = jogador + computador

    # print(end='\n')

    while not escolha == 'P' and not escolha == 'I':
        print(end='\n')
        escolha = str(input('\033[31mOpção inválida.\033[m Escolha novamente: [P/I] ')).upper().strip()[0]
    
    print(f'\nVocê jogou {jogador}')
    sleep(1)
    print(f'\nO computador jogou {computador}')
    sleep(1)
    print(f'\nO total é igual a {total}')
    sleep(1)
    print('\nOu seja...\n')
    sleep(1)
    
    if escolha == 'P': # Par
        if total % 2 == 0: # É par se a sobra do total divido por 2 for igual a 0 
            print('\033[32mVocê venceu!\033[m')
            vitórias += 1
        
        else:
            print('\033[31mVocê perdeu!\033[m\n')
            break
        

    elif escolha == 'I': # Ímpar
        if total % 2 == 1:
            print('\033[32mVocê venceu!\033[m')
            vitórias += 1
        
        else:
            print('\033[31mVocê perdeu!\033[m\n')
            break
        
    print('\nVamos jogar novamente...\n')

print(f'Jogo Finalizado! Total de vitórias: {vitórias}\n')
