d = int(input('Informe a quantidade de dias foi alugado: '))
k = float(input('Informe a distancia percorrida em KM: '))
k = k*0.15
d = d*60
a = k + d
print('O valor a se pagar pelo aluguel do carro é de R$ {:.2f}'.format(a))
