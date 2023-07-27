print('\033[31mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[37mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
print('\033[0;33;44mOlá, Mundo!\033[m')

a = 3
b = 5
print(f'Os valores \033[32m{a}\033[m e \033[31m{b}\033[m.')

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m' }

