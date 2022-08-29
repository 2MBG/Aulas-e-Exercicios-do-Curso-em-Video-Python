total_mulher_20 = 0
maior_18 = 0
total_homem = 0

print(end='\n')

print('=' * 20)
print('CADASTRO DE PESSOAS')
print('=' * 20)

print(end='\n')

while True:
    nome = str(input('\033[37;1mNome:\033[m ')).strip().title()
    idade = int(input('\033[37;1mIdade:\033[m '))
    sexo = str(input('\033[37;1mSexo\033[m [\033[34;1mM\033[m/\033[m\033[35;1mF\033[m]: ')).upper().strip()[0]

    if idade >= 18:
        maior_18 = maior_18 + 1

    if sexo in 'M':
        total_homem += 1

    if sexo in 'F' and idade < 20:
        total_mulher_20 += 1

    print(end='\n')

    continuar = str(input('\033[33mQuer continuar? [S/N]\033[m ')).upper().strip()
    
    print(end='\n')

    while not continuar == 'S' and not continuar == 'N':
        continuar = str(input('\033[31;1mOpção inválida.\033[m Quer continuar? [S/N] ')).upper().strip()
        print(end='\n')
    
    if continuar == 'N':
        print('===== ESTATÍSTICAS =====')

        print(f'\nTotal de pessoas com mais de 18 anos: {maior_18}')
        print(f'Total de homens registrados: {total_homem}')
        print(f'Total de mulheres com menos de 20 anos: {total_mulher_20}\n')
        break
