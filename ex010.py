''' Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Usa a seguinte conversão: 1 US$ = R$ 3,27. '''

dinheiro = float(input('Digite quanto dinheiro você possui em sua carteira: R$ '))
print(f'Você possui R$ {dinheiro} e consegue comprar US$ {dinheiro/3.27:.2f} com ele.')
