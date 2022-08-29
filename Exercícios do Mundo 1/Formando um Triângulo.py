print('\n\033[33;1mDESCOBRINDO SE VALORES FORMAM OU NÃO UM TRIÂNGULO:\033[m')

lado1 = float(input('\n\033[37;1mPrimeiro lado: \033[m'))
lado2 = float(input('\033[37;1mSegundo lado: \033[m'))
lado3 = float(input('\033[37;1mTerceiro lado: \033[m'))
    
# Descobrindo o tipo de triângulo
if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print('\n\033[31;1mNão é um triângulo\033[m\n')

elif (lado1 == lado2) and (lado1 == lado3) :
    print('\n\033[34;1mTriângulo Equilátero\033[m\n')

elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print('\n\033[35;1mTriângulo Isósceles\033[m\n')

else:
    print('\n\033[32;1mTriângulo Escaleno\033[m\n')
