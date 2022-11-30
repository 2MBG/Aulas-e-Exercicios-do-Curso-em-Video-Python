def título(mensagem):
    print(end='\n')
    tamanho = len(mensagem) + 4
    print('=' * tamanho)
    print(f'{mensagem}'.center(tamanho))
    print('=' * tamanho)


def leiaInt(mensagem):
    
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print('\n\033[1;31mERRO. Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def menu(lista):
    título('MENU PRINCIPAL')
    print(end='\n')
    c = 1
    for item in lista:
        print(f'\033[1;34m{c}\033[m - \033[1;32m{item}\033[m')
        c += 1

    opc = leiaInt('\n\033[1;33mEscolha uma opção:\033[m ')
    return opc
