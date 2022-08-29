número = int(input('\n\033[33;1mInforme um número para decompô-lo: \033[m'))

unidade = número // 1 % 10
dezena = número // 10 % 10
centena = número // 100 % 10
milhar = número // 1000 % 10

print(f'''\n\033[34;1mUnidade: \033[m{unidade}
\033[34;1mDezena: \033[m{dezena}
\033[34;1mCentena: \033[m{centena}
\033[34;1mMilhar:\033[m {milhar}\n''')
