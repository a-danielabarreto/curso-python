''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
 Se ele ainda vai se alistar ao serviço militar
 Se é a hota de ser alistar
 Se já passou do tempo de alistamento.

 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

genero = str(input('Qual seu gênero: M ou F? ')).upper()

if genero == 'F':
    (print('Você não precisa se alistar!'))
elif genero == 'M':
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')

    if idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} anos para o alistamento.')
        ano = ano_atual + saldo
        print(f'Seu alistamento será em {ano}.')
    elif idade > 18:
        saldo = idade - 18
        print(f'Você deveria ter se alistado há {saldo} anos')
        ano = ano_atual - saldo
        print(f'Seu alistamento foi em {ano}.')
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Opção INVÁLIDA! Tente novamente!')