'''
Crie um programa em Python que recebe como entrada quatro salários, o programa deve calcular a média salarial e exibir quais salários estão abaixo da média
'''

salarios = []
soma = 0

for i in range(4):
    salario = float(input('salario R$: '))
    soma += salario
    salarios.append(salario) #adiciona salarios em salarios

media = soma/4

print(f'Média: {media}')
for salario in salarios:
    if salario < media:
        print(f'Salário: {salario:.2f}')