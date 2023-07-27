for c in range(0, 6): #não considera o último
    print('Oi')
print('FIM')

for c in range(0, 7, 2): #não considera o último
    print('Oi')
print('FIM')

for c in range(6, 0, -1): #não considera o último
    print('Oi')
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n  #ou s += n
print(f'O somatório de todos os valores foi {s}.')
