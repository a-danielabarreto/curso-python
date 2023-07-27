''' Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media '''

nota1 = float(input('Digita a nota 1: '))
nota2 = float(input('Digita a nota 2: '))
media = (nota1 + nota2) / 2

print(f'A média nas notas {nota1:.2f} e {nota2:.2f} é {media:.2f}.')