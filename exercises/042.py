l1 = float(input('DIGITE A MEDIDA DE UM LADO DO TRIANGULO: '))
l2 = float(input('DIGITE A MEDIDA DE OUTRO LADO DO TRIANGULO: '))
l3 = float(input('DIGITE A MEDIDA FALTANTE: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print('TRIANGULO EQUILATERO')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('TRIANGULO ISÓSCELES')
    elif l1 != l2 != l3:
        print('TRIANGULO ESCALENO')
else:
    print('NÃO PODE FORMAR UM TRIANGULO')
