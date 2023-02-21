#5. Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule
# e mostre o valor do aumento e o novo salário.

salario_funcionario = float(input('Salario do funcionario: '))
aumento = float(input('Quantos porcento"%" de aumento?'))

aumentoPercentual = (aumento /100) * salario_funcionario

print('Salario com aumento:', salario_funcionario+aumentoPercentual)