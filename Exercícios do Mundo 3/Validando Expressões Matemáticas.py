expr = str(input('\nDigite a expressão: '))
pilha = []

for símbolo in expr:
    
    if símbolo == '(':
        pilha.append('(')
    
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('\nSua expressão está válida!\n')

else:
    print('\nSua expressão está errada!\n')
