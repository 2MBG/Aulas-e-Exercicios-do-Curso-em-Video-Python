sexo = str(input('\nDigite seu sexo [\033[34;1mM\033[m/\033[35;1mF\033[m]: ')).upper().strip() [0]# Pega só a primeira letra digitada

while not sexo == 'M' and not sexo == 'F':
    sexo = str(input('\033[31mDados inválidos.\033[m Por favor, informe seu sexo: ')).upper().strip()[0]
    
print(f'\nSexo {sexo} registrado com sucesso!\n')
