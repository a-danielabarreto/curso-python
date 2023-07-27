''' Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu. '''

from random import randint
from time import sleep

num = randint(0,5)

print('-' * 60)
print(f'Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-' * 60)

usuario = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if usuario == num:
    print('Você venceu! Pensamos no mesmo número!')
else:
    print(f'Você perdeu! Eu pensei no número {num} e você no número {usuario}!')


