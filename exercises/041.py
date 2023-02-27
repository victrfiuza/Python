from datetime import datetime  # substituir por date
print('-=-'*12)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=-'*12)
ano = int(input('DIGITE SEU ANO DE NASCIMENTO: '))
print('-=-'*12)
ano_atual = datetime.now().year
idade = ano_atual - ano
if idade < 9:
    print('CATEGORIA MIRIM')
elif idade >= 9 and idade < 14:
    print('CATEGORIA INFANTIL')
elif idade < 19 and idade >= 14:
    print('CATEGORIA JUNIOR')
elif idade < 20 and idade >= 19:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')
print('-=-'*12)
