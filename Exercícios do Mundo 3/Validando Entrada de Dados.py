def leiaInt(mensagem):
    ok = False
    valor = 0
    
    while True:
        number = str(input(mensagem))
        
        if number.isnumeric():
            valor = int(number)
            ok = True
        else:
            print('\n\033[1;31mErro! Digite um número intero válido.\033[m')
        if ok:
            break
    
    return valor


número = leiaInt('\nDigite um número inteiro: ')
print(f'\nVocê digitou o número {número}.\n')
