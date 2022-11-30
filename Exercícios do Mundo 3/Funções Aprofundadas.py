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


def leiaFloat(mensagem):
    
    while True:
        try:
            n = float(input(mensagem))
        except (ValueError, TypeError):
            print('\n\033[1;31mERRO: por favor, digite um  número decimal válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


número = leiaInt('\nDigite um número inteiro: ')
número1 = leiaFloat('\nDigite um número decimal: ')

print(f'\nNúmero inteiro digitado: {número}'
      f'\nNúmero decimal digitado: {número1}\n')
