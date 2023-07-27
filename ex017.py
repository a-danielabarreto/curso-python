''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa '''

import math

cateto_oposto = float(input('Digite a medida do cateto oposto: '))
cateto_adjacente = float(input('Digite a medida do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f'O comprimento da hipotenusa é de {hipotenusa}')

''' Outra forma de fazer
cateto_oposto = float(input('Digite a medida do cateto oposto: '))
cateto_adjacente = float(input('Digite a medida do cateto adjacente: '))
hipotenusa = (cateto_aposto ** 2 + cateto_adjacente **2) ** (1/2) 
print(f'O comprimento da hipotenusa é de {hipotenusa:.2f}') 
'''