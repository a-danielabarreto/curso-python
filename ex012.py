''' Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto. '''

preco = float(input('Digite o valor do produto: '))
precoComDesconto = preco * 0.95

print(f'O valor do produto com desconto de 5% é de R$ {precoComDesconto:.2f}.')