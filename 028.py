import random
from time import sleep
x = random.randrange(5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5.Tente adivinhar...')
print('-=-'*20)
sleep(3)
n = int(input('Em que número eu pensei?  '))
print('PROCESSANDO...')
sleep(2)
if x == n:
    print(f'Parabéns, você acertou, o numero era {x}')
else:
    print(f'Você errou, o numéro era {x}')
