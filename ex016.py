''' Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6'''

import math
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {math.trunc(num)}')

''' outra forma de fazer esse exercício:

from math import trunc
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}') 

'''
