#UM PROFESSOR QUE SORTEAR UM ENTRE SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE SORTEIE ALEIATORIAMENTE
#UM DELES

import random
n1 = str(input('digite seu nome: '))
n2 = str(input('digite seu nome: '))
n3 = str(input('digite seu nome: '))
n4 = str(input('digite seu nome: '))
alunos = [n1,n2,n3,n4]
print('O aluno sorteado foi: {}'.format(random.choice(alunos)))
#COMANDO CHOICE, ESCOLHE UM ITEM DA LISTA ALEATORIAMENTE
