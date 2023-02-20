salario = float(input('Informe o salario dofunconario: '))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print('O Salario do funcionario com aumento é de R$ {:.2f}'.format(novo))
