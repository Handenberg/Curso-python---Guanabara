# ESCREVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE 3 RETAS E INFORME SE ELAS FORMAM UM TRIÂNGULO

s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

if s1 <s2 + s3 and s2 < s1 +s3 and s3 < s1 + s2:
    print('As retas podem formar um triângulo!')
else:
    print('As retas NÃO podem formar um triângulo!')