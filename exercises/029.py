velocidade = int(input('Digite a velocidade: '))
if velocidade > 80:
    print(
        f'VOCÊ FOI MULTADO ! A velocidade limite é 80km/h, sua velocidade: {velocidade}')
    multa = (velocidade-80)*7
    print(f'Valor da multa: {multa}')
else:
    print('Tudo certo!')
