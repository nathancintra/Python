distancia = float(input('Digite a distancia da viagem: '))
if distancia <= 200:
    preco = distancia * 0.5
    print('O Valor a ser pago pela viagem é de R$ {:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('O Valor a ser pago pela viagem serà de R$ {:.2f}'.format(preco))
