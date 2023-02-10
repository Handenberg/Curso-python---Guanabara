#CRIE UM ALGORITMO QUE MOSTRE O ANTECESSOR E O SUCESSOR DE UM NÚMERO DIGITADO

n1 = int(input('Digite um número: '))
n2 = n1 - 1
n3 = n1 + 1
print('O antecessor do número que você digitou é {}, e o sucessor do número que você digitou é: {}' .format(n2,n3))

#OU PRINT PODE SER ESCRITO POR :
n1 = int(input('Digite um número: '))
print('O antecessor do número que você digitou é {}, e o sucessor do número que você digitou é: {}' .format(n1-1,n1+1))