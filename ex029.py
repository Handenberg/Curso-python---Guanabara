#MOSTRE A VELOCIDADE DE UM CARRO SE ELE ULTRAPASSAR 80KM MOSTRAR UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO
#E MOSTRE O VALOR DA MULTA QUE É R$ 7,00 POR KM ULTRAPASSADO

vel = int(input('Digite a velocidade do carro: '))
mul = (vel-80)*7
if vel > 80:
    print('Você foi multado!')
    print('E pagará uma multa de R$ {}'.format(mul))

else:
    print('Continue sua viagem!')
