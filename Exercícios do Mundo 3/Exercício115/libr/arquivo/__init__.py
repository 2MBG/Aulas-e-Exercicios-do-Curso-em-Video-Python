from libr.interfac import *

def arquivoExiste(nome): # Verifica se o arquivo existe
    try:
        a = open(nome, 'rt') # rt = read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome): # Cria o arquivo
    try:
        a = open(nome,  'wt+') # wt = write text. + = cria um arquivo.
        a.close()
    except:
        print('\n\033[1;31mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'\n\033[1;32mArquivo {nome} criado com sucesso!\033[m')


def lerArquivo(nome): # Lê o arquivo
    try:
        a = open(nome, 'rt')
    except:
        print('\n\033[1;31mErro ao ler o arquivo!\033[m')
    else:
        título('PESSOAS CADASTRADAS')
        print(end='\n')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}\t{dado[1]} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at') # at = append text
    except:
        print('\n\033[1;31mHouve um erro na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'\n\033[1;32mNovo registro de {nome} adicionado.\033[m')
            a.close()
