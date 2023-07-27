''' Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes '''

c1 = float(input(f'Comprimento da reta 1 em cm: '))
c2 = float(input(f'Comprimento da reta 2 em cm: '))
c3 = float(input(f'Comprimento da reta 3 em cm: '))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if c1 == c2 == c3:
        print('EQUILÁTERO!')
    elif c1 != c2 != c3 != c1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')