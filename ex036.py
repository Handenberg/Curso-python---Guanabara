#FAÇA UM PROGRAMA PARA APROVAR UM EMPRESTIMO BANCÁRIO PARA COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA
#O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE PAGARÁ A CASA.
#CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30%DO SALÁRIO OU ELA VAI NEGAR O EMPRESTIMO

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quanto anos você deseja pagar a casa? '))
quantPrest = anos * 12
vprest = casa / quantPrest
print(vprest)

if (salario*0.3) <= vprest:
    print('Sua prestação será de R$ {:.2f}'.format(vprest))
    print('Paraabéns você poderá comprar sua casa!!')

else:
    print('Sua prestação será de R$ {:.2f}'.format(vprest))
    print('Infelizmente você não poderá comprar sua casa!!!')
