''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros '''

preco = float(input('Digite o valor normal do produto: '))
condicao_pagamento = int(input('''Qual a forma de pagamento? 
[1] À vista (Dinheiro ou Cheque)
[2] À vista (Cartão)
[3] Cartão (2x)
[4] Cartão (3x ou mais) '''))

if condicao_pagamento == 1:
    total = preco * 0.9
elif condicao_pagamento == 2:
    total = preco * 0.95
elif condicao_pagamento == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela} SEM JUROS')
elif condicao_pagamento == 4:
    total = preco * 1.2
    qtd_parcelas = int(input('Quantas parcelas? '))
    parcela = total / qtd_parcelas
    print(f'Sua compra será parcelada em {qtd_parcelas}x de R$ {parcela:.2f} COM JUROS')
else:
    total = preco
    print('Opção inválida de pagamento! Tente novamente!')
print(f'O preço do produto fica R$ {total:.2f}.')

