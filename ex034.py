''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%. '''

salario = float(input('Qual o seu salário? '))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

print(f'O seu salário de R$ {salario} terá aumento de R$ {aumento:.2f}, ficando agora R${(salario + aumento):.2f}.')