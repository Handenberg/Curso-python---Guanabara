# CRIE UM PROGRAMA QUE LEIA QUANTO VOCÊ TEM NA CARTEIRA E MOSTRE QUANTOS DOLÁRES VOCÊ PoDE COMPRAR

car = float(input('Digite quanto você tem em dinheiro na carteira: R$ '))
conver = car / 5.17
print('Você conseguiria comprar: US${:.2f} Doláres' .format(conver))
