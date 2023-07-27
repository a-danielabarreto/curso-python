''' Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de
acordo com a média atingida:
Media abaixo de 5.0: REPROVADO
Media entre 5.0 e 6.9: RECUPERAÇÃO
Media 7.0 ou superior: APROVADO '''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua média é {media:.2f}.')

if media < 5:
    print('Você está REPROVADO!')
elif 5 <= media < 7.0:
    print('Você está em RECUPERAÇÃO!')
else:
    print('Parabéns, você está APROVADO!')
