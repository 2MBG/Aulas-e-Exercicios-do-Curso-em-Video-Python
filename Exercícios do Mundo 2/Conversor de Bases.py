print('\n\033[33mCONVERSOR DE BASES\033[m\n')

num = int(input('Digite um número inteiro: '))
print('''\nBases para conversão:

[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal\n''')

escolha = int(input('Digite o número da base dejesada: '))

if escolha == 1:
    print(f'\n{num} convertido na base Binária é igual a {bin(num)[2:]}.\n')

elif escolha == 2:
    print(f'\n{num} convertido na base Octal é igual a {oct(num)[2:]}.\n')

elif escolha == 3:
    print(f'\n{num} convertido na base Hexadecimal é igual a {hex(num)[2:]}.\n')

else:
    print('\nOpção inválida. Tente novamente.\n')
