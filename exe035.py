r1 = float(input('Digite o lado 1 do triangulo: '))
r2 = float(input('Digile o lado 2 do triangulo: '))
r3 = float(input('Digite o lado 3 do triangulo: '))
if (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):
    print('A retas não formam um triangulo!')
else:
    print('As retas formam um triangulo!')
