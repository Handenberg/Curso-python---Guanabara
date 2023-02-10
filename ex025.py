# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome: ')).strip()  # RETIRA OS ESPAÇOS NO INICIO E FINAL DA RESPOSTA
print('Seu nome tem silva? {}'.format('silva' in nome.lower()))

# O in É UM OPERADOR DO PYTHON

