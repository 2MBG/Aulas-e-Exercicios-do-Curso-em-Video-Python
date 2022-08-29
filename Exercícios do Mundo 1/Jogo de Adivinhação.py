from random import randint
from time import sleep

print(end='\n')
print('-' * 52)
print('\033[33;1mTENTE ADIVINHAR QUAL NÚMERO O COMPUTADOR IRÁ GERAR!\033[m')
print('-' * 52)

num1 = int(input('\n\033[37;1mDigite um número de 0 a 5: \033[m'))
num2 = randint(0,5)  # Use uniform para gerar números de ponto flutuante

while num1 < 0 or num1 > 5:
    num1 = int(input('\n\033[31;1mOpção inválida.\033[m \033[37;1mDigite um número de 0 a 5: \033[m'))

print(end='\n')

print('\033[33;1mProcessando...\033[m')
sleep(1)
print(f'\n\033[34;1mJogador:\033[m {num1}')
print(f'\n\033[35;1mCOMPUTADOR:\033[m {num2}')

if num1 == num2:
    print('\n\033[32;1mParabéns! Você acertou!\033[m\n')

else:
    print('\n\033[31;1mQue pena, você errou!\033[m\n')
