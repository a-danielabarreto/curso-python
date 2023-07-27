''' Crie um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- a media de idade do grupo
- qual é o nome do homem mais velho
- quantas mulheres tem menos de 20 anos
'''
soma_idades = 0
media = 0
maior = 0
nome_velho = ''
total_mulher_20 = 0

for pessoa in range(1,5):
    nome = str(input(f'Digite o nome da {pessoa}ª pessoa: ')).strip().upper()
    idade = int(input(f'Digite a idade da {pessoa}ª pessoa: '))
    sexo = str(input(f'Digite M ou F para gênero da {pessoa}ª pessoa: ')).strip()
    soma_idades += idade

    if pessoa == 1 and sexo in 'Mm':
        maior = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1

media = soma_idades / 4

print(f'A média da idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maior} anos e se chama {nome_velho}.')
print(f'Existem {total_mulher_20} mulheres menores que 20 anos.')

