nota1 = float(input('DIGITE A PRIMEIRA NOTA: '))
nota2 = float(input('DIGITE A SEGUNDA NOTA: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('REPROVADO')
elif media > 7:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
