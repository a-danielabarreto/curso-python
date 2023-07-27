''' Crie um programa que faço o computador jogar Jokenpô com você '''
from random import choice

jogador = str(input('Escolha entre as opções: pedra, papel ou tesoura? '))
lista = ['pedra', 'papel', 'tesoura']
print('Escolha do computador: ', end='')
computador = choice(lista)
print(computador)
vencedor = 'usuario'

if computador == 'pedra' and jogador == 'tesoura':
    vencedor = 'PC'
elif computador == 'tesoura' and jogador == 'papel':
    vencedor = 'PC'
elif computador == 'papel' and jogador == 'pedra':
    vencedor = 'PC'
elif computador == jogador:
    print('Empate!')
else:
    print(f'O computador escolheu {computador} e você escolheu {jogador}, o vencedor é {vencedor}!')
