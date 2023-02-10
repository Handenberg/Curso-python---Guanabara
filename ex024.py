#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = str(input('Digite o nome da cidade que você nasceu: ')).strip()#RETIRA OS ESPAÇOS NO INICIO E FINAL DA RESPOSTA
print(cid[:5].upper() == 'SANTO')#UPPER COLOCA TUDO EM MAIÚSCULO
