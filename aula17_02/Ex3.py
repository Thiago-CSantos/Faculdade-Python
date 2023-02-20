# 3. Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média
# ponderada dessas notas.

nota1 = float(input('1ºNota:'))
peso1 = float(input('Peso da nota 1º'))

nota2 = float(input('2ºNota:'))
peso2 = float(input('Peso da nota 2º'))

nota3 = float(input('3ºNota:'))
peso3 = float(input('Peso da nota 3º'))

mediaPonderada = ((nota1*peso1)+(nota2*peso2)+(nota3*peso3)) / (peso1+peso2+peso3)

print(mediaPonderada)
