print(end='\n')

def soma(a, b):
    s = a + b
    print(s)


# Programa Principal
# soma(a=2, b=4) Explicitando o Parâmetro

soma(4, 2)
soma(7, 3)
soma(8, 9)

#####################################

# Empacotamento de Parâmetros
print(end='\n')

def contador(* num): # Desempacota o Parâmetro
    tam = len(num)
    print(f'Há um total de {tam} números em {num}')


contador(1, 5, 6)
contador(5, 6 , 7, 8)
contador(7, 2)

#####################################
# Usando listas ao invés do Desempacotamento
print(end='\n')

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [4, 5, 6, 2, 3, 6]
dobra(valores)
print(valores)
