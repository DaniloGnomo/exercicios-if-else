n1 = int(input('Digite o primeiro numeoro: '))
n2 = int(input('Digite o segundo numeoro: '))
n3 = int(input('Digite o terceiro numeoro: '))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
    if n3 > maior:
        maior = n3

if n2 < menor:
    menor = n2
    if n3 < menor:
        menor = n3
print('{} é o numero menor!'.format(menor))
print('{} é o numero maior!'.format(maior))
