dados = dict() # Ou dados = {}
dados = {'nome':'Marcelo', 'idade':20}
print(dados['nome']) # Marcelo
print(dados['idade']) # 20
dados['sexo'] = 'M' # Cria um novo elemento (similar ao append nas listas)
del dados['idade'] # Remove um elemento
# <variável>.append(dados.copy()) # Usado para fatiar um dicionário e criar uma cópia, similar ao [:] 

print(end='\n')

###########################################################################

filme = {'título':'Need for Speed - O Filme',
        'ano':2014,
        'diretor':'Scott Waugh'
}

for key, value in filme.items():
    print(f'O {key} é {value}')

print(filme.values()) # Retorna todos os valores
print(filme.keys()) # Retorna todas as chaves
print(filme.items()) # Retorna chaves e valores juntos
