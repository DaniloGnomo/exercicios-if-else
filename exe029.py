li = 80.00
km = float(input('Digita a velocidade do automovel: '))
dif = km-li
if km > li:
    print('Você ultrapassou a velocida em {:.2f} Km por hora!'.format(km - li))
    print('Sua multa total é de R$ {:.2f} '.format(dif*7))
else:
    print('Você estava dentro do limite de velocidade!')
