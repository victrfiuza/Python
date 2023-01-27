import random
from time import sleep
x = random.randrange(5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5.Tente adivinhar...')
print('-=-'*20)
sleep(3)
n = int(input('Em que número eu pensei?  '))
print('-=-'*20)
print('\033[33mPROCESSANDO...\033[m')  # COR
print('-=-'*20)
sleep(2)
if x == n:
    print(f'\033[32mParabéns, você acertou, o numero era {x}\033[m')
else:
    print(f'\033[31mVocê errou, o numéro era\033[m {x}')
