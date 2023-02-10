#CRIE UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM, COBRANDO R$ 0,50 POR KM
# PARA VIAGENS DE ATÉ 200 KM E R$ 0,45 PARA VIAGENS MAIS LONGAS

km = float(input('Digite a quilometragem de sua viagem: '))
if km <= 200:
    print('Sua viagem terá {}KM e logo você pagará pela sua viagem, R$ {}'.format(km,(km * 0.5)))
else:
    print('Sua viagem terá {}KM e logo Você pagará pela sua viagem, R$ {}'.format(km,(km * 0.45)))