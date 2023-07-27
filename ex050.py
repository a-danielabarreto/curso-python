''' Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado foi ímpar, desconsidere-o. '''

soma = 0
cont = 0
for i in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números pares e a soma foi {soma}')

