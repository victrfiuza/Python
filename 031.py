distancia = float(input('Distancia: '))
if distancia < 200:
    passagem = distancia*0.50
    print(f'O valor da passagem é: R${passagem}')
else:
    passagem = distancia*0.45
    print(f'O valor da passagem é: R${passagem}')
