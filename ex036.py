''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
será negado. '''

valor_da_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
tempo_de_pagamento = int(input('Em quantos anos irá pagar: '))
minimo = 0.3 * salario

prestacao_mensal = valor_da_casa / (tempo_de_pagamento * 12)
print(f'Para pagar uma casa de R$ {valor_da_casa:.2f} em {tempo_de_pagamento} anos, a prestação será de {prestacao_mensal:.2f}!')

if prestacao_mensal <= minimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')

