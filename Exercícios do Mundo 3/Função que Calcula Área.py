def área(largura, comprimento):
    a = largura * comprimento
    print(f'\nA área de um terreno {largura:.1f} x {comprimento:.1f} é de {a:.1f}m².\n')


l = float(input('\nLargura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
