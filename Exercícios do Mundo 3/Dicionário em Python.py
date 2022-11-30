aluno = {}

while True:
    aluno['Nome'] = str(input('\nNome: ')).title()
    aluno['Média'] = float(input('Média: '))
    
    print(f'\nSituação de {aluno["Nome"]}:\n')
    print(f'Média: {aluno["Média"]}')
    
    if aluno['Média'] >= 7:
        print('\nAprovado!\n')
    
    else:
        print('\nReprovado!\n')
    
    break
