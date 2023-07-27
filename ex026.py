''' Faça um programa que leia uma frase pelo teclado e mostre:
a. Quantas vezes aparece a letra "A"
b. Em que posição ela aparece a primeira vez
c. Em que posição ela aparece a última vez
'''

frase = str(input('Digite uma frase: ')).strip().upper()

# a
print(frase.count('A'))

# b
print(frase.find('A')+1)

# c
print(frase.rfind('A')+1)

