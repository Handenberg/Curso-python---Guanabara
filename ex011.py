#CRIE UM PROGRAMA QUE LEIA A LARGURA A ALTURA DE UMA PAREDE , CALCULE A AREA E MOSTRA QUANTIDADE DE TINTA A SER GASTA
lar = float(input('Digite a largura da área a ser pintada: '))
alt = float(input('Digite a altura da área a ser pintada: '))
area = lar * alt
tinta = (area / 2)
print('A área a ser pintada é de: {:.2f}m²  e você precisará de {:.1f} litros de tinta'.format(area,tinta))