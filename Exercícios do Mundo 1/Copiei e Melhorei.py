print('\n\033[33mInsira as notas das respectivas matérias:\033[m')

mt1 = float(input('\nL. Portuguesa: '))
mt2 = float(input('Matemática: '))
mt3 = float(input('L. Inglesa: '))
mt4 = float(input('Geografia: '))
mt5 = float(input('História: '))
mt6 = float(input('Biologia: '))
mt7 = float(input('Química: '))
mt8 = float(input('Física: '))
média = float((mt1+mt2+mt3+mt4+mt5+mt6+mt7+mt8)/8)

print(f'\nA média geral do aluno é {média:.1f}!')

if média > 6:
    print('\n\033[32mAPROVADO!\n\033[m')

else:
    print('\n\033[31mREPROVADO!\033[m\n')
