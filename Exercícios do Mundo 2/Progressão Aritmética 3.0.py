print('\n\033[33;1mGERADOR DE PA: DEFINITIVE EDITION\033[m')

primeiro = int(input('\n\033[34;1mPrimeiro termo:\033[m '))
razão = int(input('\033[34;1mRazão da PA:\033[m '))
termo = primeiro
contador = 1
total = 0
mais = 10

print(end='\n')

while mais != 0:
    
    total = total + mais
    
    while contador <= total:
        
        print(f'{termo} → ', end='')
        termo = termo + razão
        contador = contador + 1

    print('PAUSA')
    print(end='\n')
    print('Digite \033[32;1m0\033[m para encerrar.\n')

    mais = int(input('\033[33mQuantos termos você quer mostrar a mais?\033[m '))

print(f'\nProgressão finalizada com \033[35;1m{total}\033[m termos mostrados.\n')
