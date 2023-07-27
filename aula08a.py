import math
# ou from math import sqrt (se fizer assim não precisa colocar math.sqrt() e sim sqrt()

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raiz de {num} é igual a {raiz:.2f}')
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')
print(f'A raiz de {num} é igual a {math.floor(raiz)}')