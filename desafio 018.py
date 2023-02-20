import math
angulo = float(input('Informe o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o Cosseno de {:.2f}'.format(angulo, cosseno))
tang = math.tan(math.radians(angulo))
print('O angulo de {} tem a Tangente de {:.2f}'.format(angulo, tang))
