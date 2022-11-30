people = []
pessoa = {}
soma = média = 0

while True:
    pessoa.clear
    
    pessoa['nome'] = str(input('\nNome: ')).title()

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()     
        
        print(end='\n')
        
        while not pessoa['sexo'] == 'M' and not pessoa['sexo'] == 'F':
            pessoa['sexo'] = str(input('Por favor, digite M ou F: ')).upper()
            print(end='\n')

        break

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    print(end='\n')

    people.append(pessoa.copy()) # Coloca o dicionário dentro da lista

    resposta = str(input('Quer continuar? [S/N] ')).upper()
    
    while not resposta == 'S' and not resposta == 'N':
        print(end='\n')
        resposta = str(input('\033[31mOpção inválida.\033[m Quer continuar? [S/N] ')).upper()
    
    if resposta == 'N':
        break
média = soma / len(people)

print(f'\nForam cadastradas {len(people)} pessoas.')
print(f'A média de idade é de {média:.0f} anos.')

print('Mulheres cadastradas: ', end='')
for p in people:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

print('Pessoas que estão acima da idade média: ', end='')
for p in people:
    if p['idade'] > média:
        print(f'{p["nome"]}; ', end='')
print()
