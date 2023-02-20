from random import randint
from time import sleep
computador = randint(0,5) #faz o pc escolher um numero aleatorio RANDINT
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5, Tente advinhas...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) #jogador tenta advinhas
print('Processando...')
sleep(2)
if jogador == computador:
    print('Parabens você acertou')
else:
    print('Vpcê errou, eu pensei no numero {}, e você disse {}!'.format(computador, jogador))
