def fatorial(n=0, show=False):
    
    print(end='\n')
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor Fatorial de um número n.
    '''

    f = 1
    for c in range(n, 0, -1):
        
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            

        f *= c
    return f


num = int(input('\nDigite um número para ver o seu fatorial: '))
print(fatorial(num, show=True))

# help(fatorial)
