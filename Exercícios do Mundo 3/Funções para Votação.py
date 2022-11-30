def voto():
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - nascimento
    
    if idade < 16:
        return print(f'\nCom {idade} anos você não pode votar!\n')
    
    elif idade >= 16 and idade < 18 or idade >= 65:
        return print(f'\nCom {idade} anos seu voto é opcional!\n')
    
    elif idade >= 18 and idade < 65:
        return print(f'\nCom {idade} anos seu voto é obrigatório!\n')


nascimento = int(input('\nEm que ano você nasceu? '))
voto()
