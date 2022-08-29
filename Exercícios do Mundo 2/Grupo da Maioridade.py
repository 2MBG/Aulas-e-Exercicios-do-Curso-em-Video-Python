from datetime import date

ano_atual = date.today().year
total_maior = 0
total_menor = 0

for pessoa in range(1, 8):
    
    nascimento = int(input(f'\n\033[33;1mEm que ano a {pessoa}ª pessoa nasceu?\033[m '))
    idade = ano_atual - nascimento

    if idade >= 21:
        total_maior += 1
    elif idade < 21:
        total_menor += 1

print(f'\nAo todo tivemos \033[32;1m{total_maior}\033[m pessoas maiores de idade!')
print(f'E tivemos \033[34;1m{total_menor}\033[m pessoas menores de idade!\n')
