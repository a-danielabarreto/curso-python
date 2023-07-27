''' Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. '''

import math

angulo = float(input('Digite o ângulo: '))

cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tagente = math.tan(math.radians(angulo))

print(f'O ângulo {angulo} possui seno igual a {seno:.2f}, cosseno igual a {cosseno:.2f} e tangente igual a {tagente:.2f}')