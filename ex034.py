#FAÇA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E QUE SE O SALARIO FOR MAIOR QUE 1250 CALCULE UM AUMENTO DE 10%
#SE O SALARIO FOR MENOR QUE 1250, CALCULE O AUMENTO COM 15%

sal = float(input('Digite seu salário: '))
if sal <=1250:
    novo = sal + (sal * 0.15)
else:
    novo = sal + (sal * 0.10)
print('Você ganhava R$ {} e agora seu novo salário será de R$ {:.2f}'.format(sal,novo))



