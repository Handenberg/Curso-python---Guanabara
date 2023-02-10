# CRIE UM ALGORITMOS QUE LEIA UM NÚMERO EM METROS, MOSTRE O RESULTADO EM CM E MM

m = int(input("digite a quantidade de metros: "))
cm = m * 100
mm = m * 1000
print('{} metros em centimetros é igual: {} cm'.format(m, cm))
print('{} metros em milimetros é de: {} mm'.format(m, mm))
