num = int(input('Digite o ano desejado: '))
res4 = num % 4
resc = num % 100
if res4 == 0 and resc != 0:
    print('O ano é bissexto')
else:
    print('O Ano não é bissexto')
