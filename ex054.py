''' Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
nao atingiram a maioridade e quantas ja sao maiores. '''
from datetime import date

atual = date.today().year
maiores = 0
menores = 0

for i in range(1, 8):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = atual - ano
    if idade < 21:
        menores += 1
    else:
        maiores += 1
print(f'Das sete pessoas, {maiores} são de maior e {menores} ainda não atingiram a maioridade.')



