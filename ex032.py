''' Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO. '''

# Qualquer ano que seja uniformemente divisível por 4 é um ano bissexto: por exemplo, 1988, 1992 e 1996 são anos bissextos.

from datetime import date
ano = int(input('Digite um ano: (coloque 0 para analisar o ano atual) '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO!')