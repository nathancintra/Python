vel = float(input('Informe a velocidade do carro: '))
if vel > 80:
    print('Você foi multado!')
    multa = (vel - 80)*7
    print('Você devera pagar uma multa no valor de R$ {:.2f}'.format(multa))
print('Dirija com segurança!')
