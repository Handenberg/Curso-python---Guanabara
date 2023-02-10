#FACA UM PROGRAMA QUE LEIA UM ANGULO E DÊ O VALOR DO SEN E CON

import math
an = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
rad = math.radians(an)

print('O ângulo {}, possui o SENO de {:.2f}, o COS de {:.2f} e a TAN de {:.2f}'.format(an, sen, cos, tan))
print('O valor do ângulo em RAD é', rad)

