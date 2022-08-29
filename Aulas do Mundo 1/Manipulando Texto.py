# Fatiamento de strings
frase = ('Curso em Vídeo Python')

print(frase [5:])


# Descobrindo o tamanho da string
frase = ('Curso em Vídeo Python')

print(len(frase))


# Contando quantas letras específicas possui na frase
frase = ('Curso em Vídeo Python')

print(frase.count('o'))
print(frase.upper().count('O'))


# Trocando palavras
frase = ('Curso em Vídeo Python')
# frase = frase.replace('Python' , 'Android') para mudar efetivamente a string

print(frase.replace('Python' , 'Android'))


# Encontrando uma palavra na string

# Também é possível encontrar utlizando o lower e o upper (frase.lower().find('Curso'))
frase = ('Curso em Vídeo Python')

print('Curso' in frase) # Pergunta se tal palavra existe na string
print(frase.find('Curso')) # Mostra a posição da palavra na string


# Transfromando string em lista
frase = ('Curso em Vídeo Python')
dividido = frase.split()

print(dividido [3])
print(dividido [2] [3]) # Mostra primeiro a palavra depois a letra


# Retirando espaços indesejados com .strip()

frase = str(input('Digite algo: ')).strip()
