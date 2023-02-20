# 2. Faça um programa que receba três notas, calcule e mostre a média aritmética entre elas.

nota1 = float(input('1ºNota:'))
nota2 = float(input('2ºNota:'))
nota3 = float(input('3ºNota:'))

media = (nota1 + nota2 + nota3) / 3
print('media: ', media)
print('media arredondada: ', round(media))
