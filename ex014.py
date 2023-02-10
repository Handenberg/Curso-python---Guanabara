#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite a temperatura em Celsius: '))
f = ((9 * c)/5) + 32
print('A conversão de {} cº é igual a {} f'.format(c, f))