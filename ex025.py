''' Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. '''

pessoa = str(input('Digite o nome de uma pessoa: ')).strip()

print('SILVA' in pessoa.upper())

print(pessoa.upper().__contains__('SILVA'))


