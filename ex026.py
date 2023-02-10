#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome = str(input('Digite seu nome completo: ')).lower().strip()
print('A letra A aparece {} vezes no seu nome!'.format(nome.count('a')))
print('A letra A foi encontrada a primeira vez na posição {}'.format(nome.find('a')))
print('A letra A foi encontrada pela última vez na posição {}'.format(nome.rfind('a')))