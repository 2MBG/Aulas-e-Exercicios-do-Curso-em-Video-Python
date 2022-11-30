def contador(i, f, p):
    # Docstring:
    '''
    ->Faz uma contagem e mostra na tela.
    :parâmetro i: início da contagem
    :parâmetro f: fim da contagem
    :parâmetro p: passo da contagem
    :return: sem retorno
    '''
    
    print(end='\n')
    c = i
    while c <= f:
        print(f'{c}', end=', ')
        c += p
    print('FIM!\n')

contador(0, 10, 2)

# help(contador) #Chamar a Docstring

############################################

# Escopo de Variáveis

def teste():
    x = 0 # Variável local
    print(f'Na função teste, o x vale {x}')
    print(f'Na função teste, o n vale {n}')

n = 2 # Variável global
print(f'No programa principal, o n vale {n}')
teste()

############################################
print(end='\n')

# Utilizando variável global dentro de uma função

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro da função vale {a}')
    print(f'B dentro da função vale {b}')
    print(f'C dentro da função vale {c}')

a = 5
teste(a)
print(f'A fora da função vale {a}')

############################################
print(end='\n')

# Comando return

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(2, 5, 8)
r2 = somar(4, 7, 9)
r3 = somar(9, 5, 1)

print(f'Os resultados foram {r1}, {r2} e {r3}')

# Ex. Fatorial 4: 4 * 3 * 2 * 1 = 24
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(6)
f2 = fatorial(4)
f3 = fatorial(5)

print(f'Os resultados foram {f1}, {f2} e {f3}')
