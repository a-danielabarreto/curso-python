''' Crie um programa que leia o nome completo de uma pessoa e mostre:
a. O nome com todas as letras maiusculas;
b. O nome com todas as letras minúsculas;
c. Quantas letras ao todo (sem considerar espaços);
d. Quantas letras tem o primeiro nome;
 '''

nome = str(input('Digite o seu nome completo: ')).strip()

# a
print(f'Seu nome em maiusculas é {nome.upper()}')

# b
print(f'Seu nome em minusculas é {nome.lower()}')

# c
print(f'Seu nome ao todo tem {len(nome)-len(" ")}')

# d
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e ele tem {len(nome[0])}')
