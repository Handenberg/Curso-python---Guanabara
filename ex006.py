#CRIE UM ALGORITIMO QUE CALCULE O DOBRO, O TRIPLO E A RAIZ QUADRADA DE UM NÚMERO

n1 = int(input('Digite um número: '))
d1 = n1 * 2
t1 = n1 * 3
r1 = n1 ** (1/2)
print('O dobro do número é : {}, \no triplo do número é: {}, \ne sua raiz quadrada é: {:.2f}'.format(d1, t1, r1))
# USANDO \n QUEBRA UMA LINHA
# USANDO :.2f DENTRO DAS CHAVES, LIMITA O NÚMERO DECIMAL EM 02 CASAS FLUTUANTES
