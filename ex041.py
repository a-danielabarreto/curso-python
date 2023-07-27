''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
até 9 anos: MIRIM
até 14 anos: INFANTIL
até 19 anos: JUNIOR
até 25 anos: SENIOR
acima: MASTER '''

from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print(f'Sua idade é de {idade} anos em {atual}.')

if idade <= 9:
    print('Sua categoria é: MIRIM')
elif idade <= 14:
    print('Sua categoria é: INFANTIL')
elif idade <= 19:
    print('Sua categoria é: JUNIOR')
elif idade <= 25:
    print('Sua categoria é: SENIOR')
else:
    print('Sua categoria é: MASTER')
