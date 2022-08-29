nome = str(input('\n\033[33mDigite seu nome completo: \033[m')).strip()
silva = 'Silva' in nome.title()

print(f'\nPossui Silva no nome desse usuário? {silva}!\n')
