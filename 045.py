from random import randint, randrange
print('PEDRA PAPEL TESOURA')
y = int(input('ESCOLHA UMA DAS OPÇÕES:\n[1]PEDRA\n[2]PAPEL\n[3]TESOURA]\n'))
pc = randint(1, 3)
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
