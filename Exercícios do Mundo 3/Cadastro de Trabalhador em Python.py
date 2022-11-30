from datetime import date
dados = {}

while True:
    print(end='\n')
    dados['nome'] = str(input('Nome completo: ')).title()
    dados['nascimento'] = int(input('Ano de nascimento: '))
    dados['ctps'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
    
    if dados['ctps'] == 0:
        ano = date.today().year
        idade = ano - dados['nascimento']
        
        print(f'\nNome: {dados["nome"]}\n'
        f'Idade: {idade} anos\n'
        'CTPS: Não possui.\n')
    
    else:
        ano = date.today().year
        idade = ano - dados['nascimento']
        
        dados['contratado'] = int(input('Ano de contratação: '))
        dados['salário'] = float(input('Salário: '))
        dados['aposentadoria'] = idade + ((dados['contratado'] + 35) - date.today().year)

        print(f'\nNome: {dados["nome"]}\n'
        f'Idade: {idade} anos\n'
        f'CTPS: {dados["ctps"]}\n'
        f'Contratação: {dados["contratado"]}\n'
        f'Salário: R${dados["salário"]:.2f} reais\n'
        f'Aposentadoria: Irá se aposentar aos {dados["aposentadoria"]} anos\n')

    break
