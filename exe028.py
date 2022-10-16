import random
from time import sleep
num = random.randint(0, 5)
print('É hora do jogo, tente acertar o meu numero')
sleep(2)
print('Escolhendo um numero.......')
sleep(2)
print('+'*28)
numu = int(input('Tente adivinhar o numero de 0 a 5: '))
if numu == num:
    print('Você Venceu, parabens!')
else:
    print('Você Perdeu! O numero era {}'.format(num))
