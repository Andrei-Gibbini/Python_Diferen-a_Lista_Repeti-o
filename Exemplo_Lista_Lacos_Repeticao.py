'''
Crie um programa em Python que recebe como entrada quatro salários, o programa deve calcular a média salarial e exibir quais salários estão abaixo da média
'''

salarios = [0,0,0,0]
soma = 0
i = 0 #controle de looping
#preenchendo a lista de salários
while i < 4:
    salarios[i] = float(input('Salário R$: '))
    soma +=salarios[i]
    i+=1

#calcular a média
media = soma/4

print(f'Media Salarial: {media:.2f}')

#imprimir os salários que estão abaixo da média
i = 0
while i<4:
    if salarios[i] < media:
        print(f'Salário menor do que a média: {salarios[i]:.2f}')
    i+= 1

'''
Programa em lista com laços de repetição. Esse é o formato mais curto, fácil e prático de fazer.
'''