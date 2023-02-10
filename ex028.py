from random import randint
from time import sleep

num = int(input('Tente descobrir o número que o computador escolheu de 0 a 5, digite seu número: '))
numpc = int(randint(0,5))
if num == numpc:
    print('PROCESSANDO......')
    sleep(2)
    print('Parabéns, o número escolhido pelo computador foi {}'.format(numpc))
else:
    print('PROCESSANDO......')
    sleep(2)
    print('Não foi desta vez,eu pensei no número {}. Tente novamente!'.format(numpc))

