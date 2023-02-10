# CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL E APRESENTE NA TELA APENAS SUA PARTE INTEIRA, EX: 6.127 E MOSTRE APENAS 6

import math
n1 = float(input("Digite um número real: "))
n2 = math.trunc(n1)
print('o Número {} sem as casas decimais é: {}'.format(n1,n2))
#OU
print('o Número {} sem as casas decimais é: {}'.format(n1,math.trunc(n2)))

#OU

from math import trunc
n1 = float(input("Digite um número real: "))
print('o Número {} sem as casas decimais é: {}'.format(n1,trunc(n2)))
