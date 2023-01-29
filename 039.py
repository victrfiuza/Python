from datetime import datetime
nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - nascimento
if idade < 18:
    print('VOCE AINDA VAI SE ALISTAR!')
    tempo = 18 - idade
    print(f'FALTA {tempo} ANOS PARA SE ALISTAR')
elif idade > 18:
    print('JA PASSOU DO TEMPO DE SE ALISTAR!')
    tempo = idade - 18
    print(f'JA PASSOU {tempo} ANOS DE SE ALISTAR!')
else:
    print('ESTA NA HORA DE SE ALISTAR!')
