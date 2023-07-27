''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo
 com a tabela abaixo:
 abaixo de 18.5: abaixo do peso
 entre 18.5 e 25: peso ideal
 25 até 30: sobrepeso
 30 até 40: obesidade
 acima de 40: obesidade mórbida '''

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metro: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.1f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')


