from calendar import isleap

ano = int(input('Digite o ano desejado: '))

if isleap(ano):
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')
