# CRIE UM PROGRAMA QUE MOSTRE O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# COM TODAS LETRAS MAIÚSCULAS
# COM TODAS MINUSCULAS
# CONTE TODAS AS LETRAS SEM CONTAR OS ESPAÇOS
# QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str(input('Digite seu nome completo: ')).strip()
print('Todas as letras maiúsculas', nome.upper())
print('Todas as letras minúsculas', nome.lower())
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))#-NOME.COUNT(' ') RETIRA OS ESPAÇOS DO NOME
separa = nome.split()
print('Seu primeiro nome {}, tem {} letras'.format(separa[0], len(separa[0])))

