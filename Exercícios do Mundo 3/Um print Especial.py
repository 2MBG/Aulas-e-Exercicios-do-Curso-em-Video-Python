def escreva(mensagem):
    tamanho = len(mensagem) + 4 # O 4 adiciona bordas extras
    print('-' * tamanho)
    print(f'  {mensagem}')
    print('-' * tamanho)


escreva('Marcelo Martins da Silva Araújo')
