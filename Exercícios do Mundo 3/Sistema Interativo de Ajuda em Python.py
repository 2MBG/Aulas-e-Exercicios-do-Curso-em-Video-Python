from time import sleep

def ajuda(com):
    título(f'Acessando o manual do comando {com}')
    sleep(1)
    help(com)

def título(mensagem):
    print(end='\n')
    tamanho = len(mensagem) + 4
    print('=' * tamanho)
    print(f'  {mensagem}')
    print('=' * tamanho)


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP')
    comando = str(input('\nFunção ou Biblioteca: '))
    
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    
título('ATÉ LOGO!')
