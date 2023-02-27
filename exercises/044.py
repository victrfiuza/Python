preco = float(input('DIGITE O VALOR DO PRODUTO: R$'))
print(
    '\nSELECIONE A FORMA DE PAGAMENTO:\n\n[1]À VISTA DINHEIRO/CHEQUE (10% DE DESCONTO)\n[2]À VISTA NO CARTÃO(5% DE DESCONTO)\n[3]EM ATÉ 2X NO CARTÃO(PREÇO NORMAL)\n[4]3X OU MAIS NO CARTÃO(20% DE JUROS)')
forma = int(input(''))
if forma == 1:
    desconto = (preco*10) / 100
    preco = preco - desconto
    print(f'VALOR À VISTA NO DINHEIRO/CHEQUE: R${preco}')
if forma == 2:
    desconto = (preco*5) / 100
    preco = preco - desconto
    print(f'VALOR À VISTA NO CARTÃO: R${preco}')
if forma == 3:
    print(f'VALOR TOTAL: R${preco}')
if forma == 4:
    desconto = (preco*20) / 100
    preco = preco + desconto
    print(f'3X OU MAIS NO CARTÃO: R${preco}')
