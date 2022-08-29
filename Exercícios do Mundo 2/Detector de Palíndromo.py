print('\n\033[33;1mPALÍNDROMO OU NÃO?\033[m\n')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
tudo_junto =  ''.join(palavras)
inverso = ''

for letra in range(len(tudo_junto) -1, -1, -1): # Contagem reversa
    inverso += tudo_junto[letra]

if inverso == tudo_junto:
    print('\nA frase digitada é um palíndromo!\n')

else:
    print('\nA frase digitada não é um palíndoromo!\n')


# USANDO FATIAMENTO:

'''frase = str(input('\nDigite uma frase: ')).strip().upper()
palavras = frase.split()
tudo_junto =  ''.join(palavras)
inverso = tudo_junto[::-1]

if inverso == tudo_junto:
    print('\nA frase digitada é um palíndromo!\n')
else:
    print('\nA frase digitada não é um palíndoromo!\n')'''
