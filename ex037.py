''' Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
base de conversão:
1 para binário
2 para octal
3 para hexadecimal '''

num = int(input('Digite um número inteiro: '))

print('Escolha a base de conversão: ')
print('1 - Converter para Binário: ')
print('2 - Converter para Octal: ')
print('3 - Converter para Hexadecimal: ')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a: {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a: {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a: {hex(num)[2:]}')
else:
    print('Opção inválida! Tente novamente!')



