''' Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar
um triângulo. '''

c1 = float(input(f'Comprimento da reta 1 em cm: '))
c2 = float(input(f'Comprimento da reta 2 em cm: '))
c3 = float(input(f'Comprimento da reta 3 em cm: '))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')

