nota1 = float(input('\nHistória: '))
nota2 = float(input('Português: '))
nota3 = float(input('Matemática: '))
nota4 = float(input('Geografia: '))
nota5 = float(input('Ciências: '))
nota6 = float(input('Física: '))
nota7 = float(input('Espanhol: '))
nota8 = float(input('Inglês: '))
nota9 = float(input('Biologia: '))
nota10 = float(input('Química: '))

média = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10) / 10
média2 = print(f'\nSua média é \033[37;1m{média}\033[m')

if média < 5.0:
    print('\nVocê está \033[31;1mREPROVADO!\n\033[m')

elif média >= 7.0:
    print('\nVocê está \033[32;1mAPROVADO!\033[m\n')

elif média >= 5 and média < 7:
    print('\nVocê está de \033[33;1mRECUPERAÇÃO!\033[m\n')
