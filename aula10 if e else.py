#nome = str(input('Digite seu nome: ')).title().strip()
#if nome == 'Gustavo':
 #   print('Que nome lindo você tem!')
#else:
 #   print('Olá {}, seu nome é comum!'.format(nome))
#print('Bom dia {}!'.format(nome))

#_______________________________________________

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1+nota2)/2
print('Sua média final foi {:.2}'.format(media))
if media >= 7.0:
    print('Parabéns, você foi aprovado!')
else:
    print('Você foi reprovado!')



