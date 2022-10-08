saque = int(input('\nQuanto você deseja sacar? R$ '))
total = saque
cédula = 50
total_cédulas = 0

print(end='\n')

while True:
    if total >= cédula:
        total -= cédula
        total_cédulas += 1
    
    else:
        if total_cédulas > 0:
            print(f'Total de {total_cédulas} cédulas de R${cédula}')
        
        if cédula == 50: # Vai tirando até não dar mais
            cédula = 20
        
        elif cédula == 20: # Vai tirando até não dar mais
            cédula = 10
        
        elif cédula == 10: # Vai tirando até não dar mais
            cédula = 5
        
        elif cédula == 5:  # Vai tirando até não dar mais
            cédula = 1
        
        total_cédulas = 0

        if total == 0:
            break

print('\nSaque realizado! Volte sempre!\n')
