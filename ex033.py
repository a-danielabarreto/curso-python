''' Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor. '''

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
