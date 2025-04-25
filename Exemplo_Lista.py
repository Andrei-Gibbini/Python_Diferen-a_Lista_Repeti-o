'''
Crie um programa em Python que recebe como entrada quatro salários, o programa deve calcular a média salarial e exibir quais salários estão abaixo da média
'''

salario = [0,0,0,0]

soma = 0
salario[0] = float(input('Salário R$: '))
soma += salario[0]
salario[1] = float(input('Salário R$: '))
soma += salario[1]
salario[2] = float(input('Salário R$: '))
soma += salario[2]
salario[3] = float(input('Salário R$: '))
soma += salario[3]

media = soma/4
print(f'media salarial: {media:.2f}')

if salario[0] < media:
    print(f'Salário abaixo da média: {salario[0]:.2f}')
if salario[1] < media:
    print(f'Salário abaixo da média: {salario[1]:.2f}')
if salario[2] < media:
    print(f'Salário abaixo da média: {salario[2]:.2f}')
if salario[3] < media:
    print(f'Salário abaixo da média: {salario[3]:.2f}')

'''
Esse formato é o correto, deve-se usar lista com laço de repetição
Facilita muito a criação e execução
'''