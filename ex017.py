#CRIE UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO, DO CATETO ADJACENTE , CALCULE E MOSTRE A MEDIDA DA HIPOTENUSA
import math
cato = float(input('Digite o valor do cateto oposto: '))
cata = float(input('Digite o valor do cateto adjacente: '))
hip = math.sqrt(cato**2 +cata**2)
print('A hipoptenusa tem valor de: {:.2f}'.format(hip))

#OU

import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(co, ca)
print("A hipotenusa tem valor de: {:.2f}".format(hip))

#OU

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co, ca)
print("A hipotenusa tem valor de: {:.2f}".format(hip))