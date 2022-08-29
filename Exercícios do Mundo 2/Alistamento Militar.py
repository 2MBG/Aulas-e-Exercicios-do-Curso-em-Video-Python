from datetime import date

idade = int(input('\nEm que ano você nasceu? '))
ano = date.today().year
ano2 = ano - idade
ano3 = ano2 - 18
ano4 = 18 - ano2
print('''\nSexo:

\033[37;1m[1]\033[m \033[34;1mHomem\033[m
\033[37;1m[2]\033[m \033[35;1mMulher\033[m\n''')


sexo = int(input('Digite o número correspondente: '))

while not sexo == 1 and not sexo == 2:
    print(end='\n')
    sexo = int(input('\033[31mOpção inválida.\033[m Digite o número correspondente: '))

print(end='\n')

if sexo == 2:
    print('\033[32;1mSeu alistamento militar não é obrigatório!\033[m\n')

elif ano2 == 18:
    print('\033[34;1mVocê deve se alistar no Exército Brasileiro ainda este ano!\033[m\n')

elif ano2 > 18:
    print(f'\033[31;1mSeu alistamento militar está atrasado já faz {ano3} ano(s). ' 
    'Apresente-se ao quartel para regularizar sua situação!\033[m\n')

elif ano2 < 18: 
    print(f'\033[33;1mAinda falta {ano4} ano(s) para você se alistar no Exército Brasileiro!\033[m\n')
