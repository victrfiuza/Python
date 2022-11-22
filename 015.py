dias = float(input('dias alugados: '))
kmr = float(input('km rodados: '))
dias = dias*60
kmr = kmr*0.15
print(f'pagar: R${dias+kmr}')
