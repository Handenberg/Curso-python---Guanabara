#UM PROFESSOR QUE SORTEAR UM ENTRE SEUS QUATRO ALUNOS PARA APRESENTAR UM TRABALHO. FAÇA UM PROGRAMA QUE SORTEIE ALEIATORIAMENTE
#UM DELES E MOSTRE A ORDEM SORTEADA
#USE RANDOM.

import random
n1 = str(input('digite seu nome: '))
n2 = str(input('digite seu nome: '))
n3 = str(input('digite seu nome: '))
n4 = str(input('digite seu nome: '))
alunos = [n1,n2,n3,n4]
random.shuffle(alunos) #SHUFFLE EMBARALHA A LISTA
print('A ordem de apresentação será:', alunos)