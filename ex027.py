''' Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente.

Ex:
Ana Maria de Souza

primeiro = Ana
último = Souza

'''

nome = str(input('Nome completo: ')).strip()
nome = nome.split()

print(nome)
print(f'primeiro: {nome[0]}')
print(f'último: {nome[-1]}')