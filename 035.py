r1 = float(input('reta 1:'))
r2 = float(input('reta 2:'))
r3 = float(input('reta 3:'))
if (r1 + r2 > r3) & (r2 + r3 > r1) & (r1 + r3 > r2):
    print('Pode formar um triangulo')
else:
    print('Não pode formar um triangulo')
