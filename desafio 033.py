a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Teceiro valor: '))
#Verificando qual é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando qual é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O 8menor valor digitado foi {} '.format(menor))
print('O maior valor digitado foi {}'.format(maior))
