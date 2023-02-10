#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É PAR OU ÍMPAR

num = int(input('Digite um numero: '))
if (num % 2) == 0:
    print('O número {} é um número PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))
