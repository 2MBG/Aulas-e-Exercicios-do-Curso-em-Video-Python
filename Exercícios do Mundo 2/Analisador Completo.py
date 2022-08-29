soma_idade = 0
média_idade = 0
maior_idade_homem = 0
nome_do_velho = ''
total_mulher_20 = 0

print(end= '\n')

for pessoa in range(1, 5):
    print(f'\033[33m===== {pessoa}ª PESSOA =====\033[m')
    
    nome = str(input('\033[37;1mNome:\033[m ')).strip().title()
    idade = int(input('\033[37;1mIdade:\033[m '))
    sexo = str(input('\033[37;1mSexo\033[m [\033[34;1mM\033[m/\033[m\033[35;1mF\033[m]: ')).upper().strip()[0]
    soma_idade = soma_idade + idade # +=
    
    print('\n')

    if pessoa == 1 and sexo == 'M': 
        maior_idade_homem = idade
        nome_do_velho = nome

    if sexo in 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_do_velho = nome

    if sexo in 'F' and idade < 20:
        total_mulher_20 = total_mulher_20 + 1 # +=

média_idade = soma_idade / 4

print(f'A média de idade do grupo é de {média_idade:.1f} anos!')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_do_velho}.')
print(f'Possui um total de {total_mulher_20} mulhere(s) com menos de 20 anos.\n')
