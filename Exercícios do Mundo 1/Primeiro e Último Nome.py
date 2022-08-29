nome = str(input('\nDigite seu nome completo: ')).strip().title()
nome2 = nome.split() # Transformando em lista

print(f'\nSeu primeiro nome é {nome2[0]}!')
print(f'Seu último nome é {nome2[len(nome2)-1]}!\n')
