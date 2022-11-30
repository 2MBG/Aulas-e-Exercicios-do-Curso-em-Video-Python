def notas(*n, situação=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param situação: valor opcional, indicando se deve ou não adicionar a situação do aluno.
    :return: dicionário com várias informações sobre a situação do aluno.
    '''

    r = dict()
    r ['total'] = len(n)
    r ['maior'] = max(n)
    r ['menor'] = min(n)
    r ['média'] = sum(n)/len(n)

    if situação:
        if r ['média'] >= 7:
            r ['situação'] = 'BOA'
        elif r ['média'] >= 5:
            r ['situação'] = 'RAZOÁVEL'
        else:
            r ['situação'] = 'RUIM'
    return r


resposta = notas(6.5, 9.5, 8.5, situação=True)
print(resposta)
# help(notas)
