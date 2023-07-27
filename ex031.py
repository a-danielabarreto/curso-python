''' Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 por km para viagens mais longas. '''

distancia = float(input('Qual a distância da viagem em km? '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'O preço da passagem é de R$ {preco:.2f}.')

