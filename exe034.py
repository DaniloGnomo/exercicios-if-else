sal = float(input('Digite o valor do salario: '))
dz = sal*10/100
qz = sal*15/100
if sal > 1250:
    print('Seu novo Salario é R$ {:.2f}'.format(sal+dz))
    print('Você teve uma aumento de R$ {:.2f}'.format(dz))
else:
    print('Seu novo Salario é R$ {:.2f}'.format(sal+qz))
    print('Você teve uma aumento de R$ {:.2f}'.format(qz))
