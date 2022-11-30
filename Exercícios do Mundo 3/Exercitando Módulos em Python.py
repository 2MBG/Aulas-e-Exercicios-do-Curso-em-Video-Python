import moeda

preço = float(input('\nDigite um preço: '))

print(f'\nCom um aumento de 10%, o preço passa a ser R${(moeda.aumentar(preço,True))}')
print(f'Com uma redução de 13%, o preço passa a ser R${(moeda.diminuir(preço, True))}')
print(f'O dobro de R${moeda.form(preço)} é R${(moeda.dobro(preço, True))}')
print(f'A metade de R${moeda.form(preço)} é R${(moeda.metade(preço, True))}\n')
