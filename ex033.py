# FAÇA UM PROGRAMA QUE LEIA 3 NPUMEROS E MOSTRE QUAL O MAIOR E QUAL O MENOR

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
# VERIFICANDO QUEM É O MENOR
if a < b and a < c:
    menor = a
if c < b and c < a:
    menor = c
if b < a and b < c:
    menor = b
# VERIFICANDO QUEM É O MAIOR
if a > b and a > c:
    maior = a
if c > b and c > a:
    maior = c
if b > a and b > c:
    maior = b
print('O menor valor digital foi {}.'.format(menor))
print('O maior valor digital foi {}.'.format(maior))
