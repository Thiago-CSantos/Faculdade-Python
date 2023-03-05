# Faça um programa que calcule e mostre a área de um círculo. Sabe-se que: Área = 3.14 * raio^2.

raio = float(input('Raio: '))

area = 3.14 * pow(raio, 2)
# area = 3.14 * raio * raio

print(area)