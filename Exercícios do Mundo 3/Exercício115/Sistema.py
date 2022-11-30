from libr.interfac import *
from libr.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar nova pessoa',
                     'Listar pessoas cadastradas', 
                     'Sair do Sistema'])
    
    if resposta == 1:
        # Opção de cadastrar uma nova pessoa.
        título('NOVO CADASTRO')
        nome = str(input('\n\033[1;34mNome:\033[m ')).title()
        idade = leiaInt('\033[1;34mIdade:\033[m ')
        cadastrar(arq, nome, idade)
        
    elif resposta == 2:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    
    elif resposta == 3:
        print('\nSaindo do sistema...')
        sleep(1.5)
        print('\nAté logo!\n')
        break
    
    else:
        print('\n\033[1;31mERRO! Digite uma opção válida!\033[m\n')
    sleep(1)
