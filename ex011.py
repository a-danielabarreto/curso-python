''' Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
 tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m². '''

largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))
area = largura * altura
quantidade = area / 2

print(f'A área da parede é {area} m² e a quantidade de tinta necessária é {quantidade} litros.')