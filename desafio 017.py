from math import hypot
co = float(input('Infomre o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
