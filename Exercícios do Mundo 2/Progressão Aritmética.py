primeiro = int(input('\n\033[36;1mPrimeiro termo:\033[m '))
razão = int(input('\033[36;1mRazão:\033[m ')) # De quanto em quanto serão contados
décimo = primeiro + 10 * razão

print(end='\n')

for contador in range(primeiro, décimo, razão):
    print('\033[33;1m', end = '')
    print(contador, end = ' \033[36;1m→\033[m ')

print('\033[37;1mFim\033[m\n')
