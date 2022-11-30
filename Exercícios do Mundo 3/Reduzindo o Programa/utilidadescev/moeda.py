def aumentar(p=0, taxa=0, formatado=False):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param p: o preço que se quer reajustar.
    :param taxa: qual a porcentagem do aumento.
    :param formatado: escolhe se a saída será formatada ou não.
    :return: o valor reajustado, com ou sem formatação.
    '''
    
    num1 = p + (p * taxa / 100)
    return num1 if not formatado else form(num1)


def diminuir(p=0, taxa=0, formatado=False):
    '''
    -> Calcula a redução de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param p: o preço que se quer reajustar.
    :param taxa: qual a porcentagem da redução.
    :param formatado: escolhe se a saída será formatada ou não.
    :return: o valor reajustado, com ou sem formatação.
    '''

    num2 = p - (p * taxa / 100)
    return num2 if not formatado else form(num2)


def dobro(p=0, formatado=False):
    '''
    -> Calcula o dobro de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param p: o preço que se quer reajustar.
    :param formatado: escolhe se a saída será formatada ou não.
    :return: o valor reajustado, com ou sem formatação.
    '''
    
    num3 = p * 2
    return num3 if not formatado else form(num3)


def metade(p=0, formatado=False):
    '''
    -> Calcula a metade de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param p: o preço que se quer reajustar.
    :param formatado: escolhe se a saída será formatada ou não.
    :return: o valor reajustado, com ou sem formatação.
    '''
    
    num4 = p / 2
    return num4 if not formatado else form(num4)


def form(p=0):
    '''
    -> Faz a formatação de uma valor.
    :param p: valor que será formatado.
    '''
    
    return f'{p:.2f}'.replace('.', ',')

def resumo(p=0, taxa1=10, taxa2=20):
    print(end='\n')
    print('=' * 40)
    print('RESUMO DO VALOR'.center(40)) # center() não funciona com cores.
    print('=' * 40)
    
    print(f'Preço analisado: \tR$ {form(p)}')
    print(f'{taxa1}% de aumento: \tR$ {aumentar(p, taxa1, True)}')
    print(f'{taxa2}% de redução: \tR$ {diminuir(p, taxa2, True)}')
    print(f'Dobro do preço: \tR$ {dobro(p, True)}')
    print(f'Metade do preço: \tR$ {metade(p, True)}')
    print('=' * 40)
    print(end='\n')
