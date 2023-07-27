''' Escreva um programa que leia a velocidade de um carro.
 Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
 A multa vai custar R$ 7,00 por cada km acima do limite. '''

velocidade = float(input('Velocidade do carro em km: '))

if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print (f'A multa é de R$ {multa:.2f}.')
print('Tenha um bom dia! Dirija com segurança!')