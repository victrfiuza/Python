from random import randint
from time import sleep


def Header():
    print('\n', '{:^68}'.format(('\033[32mJOKENPO\033[m')))
    print('-' * 62)


Header()


def Menu():
    print('\033[033mMENU PRINCIPAL\033[m'.center(70))
    line = '°' * 16
    print(line.center(60))
    print('''[1]PEDRA
             [2]PAPEL
             [3]TESOURA'''.center(80))


Menu()


def animation():
    sleep(0.5)
    print('\n', '----------'.center(50))
    print('\033[31mJO\033[m'.center(50))
    sleep(0.5)
    print('\033[32mKEN\033[m'.center(60))
    sleep(0.5)
    print('\033[33mPO\033[m'.center(70))
    print('°°°°°°°°°°°°°°°°'.center(52))
    sleep(1)


animation()

y = int(input('ESCOLHA UMA DAS OPÇÕES:'))
pc = randint(1, 3)
if (y >= 1) and (y <= 3):
    if y == 1:
        if pc == 1:
            print('EMPATE')
        elif pc == 2:
            print('VOCê PERDEU! A MAQUINA ESCOLHEU PAPEL!')
        elif pc == 3:
            print('VOCÊ GANHOU! A MAQUINA ESCOLHEU TESOURA!')

    if y == 2:
        if pc == 1:
            print('VOCê GANHOU! A MAQUINA ESCOLHEU PEDRA!')
        elif pc == 2:
            print('EMPATE!')
        elif pc == 3:
            print('VOCÊ PERDEU! A MAQUINA ESCOLHEU TESOURA!')

    if y == 3:
        if pc == 1:
            print('VOCÊ PERDEU! A MAQUINA ESCOLHEU PEDRA!')
        elif pc == 2:
            print('VOCÊ GANHOU! A MAQUINA ESCOLHEU PAPEL!')
        elif pc == 3:
            print('EMPATE!')
else:
    print('OPCAO INVALIDA')
