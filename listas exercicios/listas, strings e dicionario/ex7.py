palavra = str(input('Digite uma palavra palíndromo'))

invertido = palavra[::-1]

if(invertido == palavra):
    print('palíndromo ='+invertido)
else:
    print('não é palíndromo')

