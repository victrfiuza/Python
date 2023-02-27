salario = float(input('Salario: '))
if salario > 1250:
    aumento = (salario*10) / 100
    print(f'Salario com aumento: {salario+aumento}')
else:
    aumento = (salario*15) / 100
    print(f'Salario com aumento: {salario+aumento}')
