print('CALCULADORA IMC')
print('-=-'*12)
peso = float(input('DIGITE SEU PESO: '))
altura = float(input('DIGITE SUA ALTURA: '))
imc = peso / (altura * altura)
print('-=-'*12)
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc <= 25:
    print('PESO IDEAL')
elif imc > 25 and imc <= 30:
    print('SOBREPESO')
elif imc > 30 and imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
