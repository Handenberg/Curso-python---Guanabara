#CRIE UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO

p1 = float(input('Digite o valor do produto que deseja: '))
Pdesc = (p1 - (p1 * 0.05))
print('Valor do produto é R${} , '
      'Se o pagamento for à vista tem 5% de desconto e seu produto sairá por R${}'.format(p1,Pdesc))

