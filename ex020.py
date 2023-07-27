''' O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. '''

import random

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

alunos = [n1, n2, n3, n4]

random.shuffle(alunos) #esse comando é para embaralhar a lista

print(f'A ordem de apresentação será :')
print(alunos)
