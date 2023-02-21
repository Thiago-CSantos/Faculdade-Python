# 6. Faça um programa que receba o salário base de um funcionário, calcule e mostre o seu salário
# a receber, sabendo-se que o funcionário tem gratificação de R$ 50,00 e paga imposto de 10%
# sobre o salário base.

salario_base = float(input('Salario base do funcionario: '))

x = salario_base * 0.10
salario_receber = (salario_base+50.00) - x

print('Salario ha receber:', salario_receber)
