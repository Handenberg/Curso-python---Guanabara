#CRIE UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E DEPOIS MOSTRE SEU NOVO SALÁRIO COM 15% DE AUMENTO

n1 = input('Digite seu nome: ')
s1 = float(input('Digite o valor do seu salário: '))
s2 = s1 + (s1 * 0.15)
print('Parabéns {}, você recebeu um aumento de 15% e seu novo salário é de R$ {}'.format(n1, s2))