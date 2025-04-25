'''
Crie um código para ler e calcular a média salarial inserida e apontar os salários menores do que a média
'''


soma = 0
salario_0 = float(input('Salário R$: '))
soma += salario_0
salario_1 = float(input('Salário R$: '))
soma += salario_1
salario_2 = float(input('Salário R$: '))
soma += salario_2
salario_3 = float(input('Salário R$: '))
soma += salario_3

media = soma/4
print(f'media salarial: {media:.2f}')

if salario_0 < media:
    print(f'Salário abaixo da média: {salario_0:.2f}')
if salario_1 < media:
    print(f'Salário abaixo da média: {salario_1:.2f}')
if salario_2 < media:
    print(f'Salário abaixo da média: {salario_2:.2f}')
if salario_3 < media:
    print(f'Salário abaixo da média: {salario_3:.2f}')

'''
Esse formato não é o correto, deve-se usar lista
'''