
frase = 'Curso em Vídeo Python'

# Manipulando texto
print(frase[9])
print(frase[9:13]) # o valor que estiver no 13 não é impresso!
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Análise
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

# Transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = '   Aprenda Python  '

print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

# Divisão
print(frase.split())

lista = ['Curso', 'em', 'Vídeo', 'Python']
print('-'.join(frase))
print('-'.join(lista))

print("""A University of the People é a primeira universidade online credenciada e 
gratuita do mundo com sede nos Estados Unidos. Esta universidade oferece programação gratuita 
para que você queira pagar mensalidades, livros, materiais do curso ou qualquer outra coisa. 
Os únicos custos são uma taxa de inscrição de $ 60 e uma taxa de avaliação de $ 100 por curso concluído. 
Todas as outras despesas são totalmente cobertas por doações e patrocinadores.""")






