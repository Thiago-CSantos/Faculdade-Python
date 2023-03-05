# Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e
# mostre a idade dessa pessoa.
from datetime import datetime

ano_nasc = int(input('Ano de nascimento: '))

ano_atual = datetime.today().year

print(ano_atual - ano_nasc)
