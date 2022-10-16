km = float(input('Digite a kilometragem da viagem: '))
tr1 = 0.50
tr2 = 0.45
if km <= 200.00:
    print('O custo total sera de R$ {:.2f}'.format(km * tr1))
else:
    print('O custo total sera de R$ {:.2f}'.format(km * tr2))
