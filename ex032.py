#FAÇA UM PROGRAMA QUE LEIA UM ANO E DIGA SE ELE É BISSEXTO.
from datetime import date

ano = int(input('Digite o ano para analisarmos se é bissexo ou digite 0 para saber o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4) == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {}, é um ano Bissexto'.format(ano))
else:
    print('O ano de {}, NÃO é um ano Bissexto'.format(ano))