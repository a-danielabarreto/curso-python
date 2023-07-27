'''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. Obs: divisivel só um 1 ou
por ele mesmo. '''

num = int(input('Digite um número inteiro: '))
contador = 0
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
print(f'O número {num} foi divisivel {total} vezes.')
if total == 2:
    print('E por isso ele É PRIMO!!')
else:
    print('E por isso ele NAO É PRIMO!!')

