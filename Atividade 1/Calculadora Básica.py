# Questão 2 da atividade introdução a Python
# Autor: Guilherme Guimarães dos Santos
# Data: 15/06/2022
from time import sleep

print(f'{" CALCULADORA ":=^60}')
print('''1 -> SOMA
2 -> SUBTRAÇÃO
3 -> MULTIPLICAÇÃO
4 -> DIVISÃO''')
opção = int(input('Escolha um número de acordo com a operação desejada: '))

print('-=' * 20)
if ((opção < 1) or (opção > 4)):
    print('Opção Inválida! ')
    sleep(0.5)
    print('Encerrando...')  
    sleep(0.5)
else:
    valor_1 = int(input('Digite um número: '))
    valor_2 = int(input('Digite outro número: '))
    operação = 0
    tipo = ''
    if opção == 1:
        tipo = 'Soma'
        operação = (valor_1 + valor_2)
        sleep(0.5)
        print(f'O valor da {tipo} entre {valor_1} e {valor_2} é igual a {operação}. ')
    elif opção == 2:
        tipo = 'Subtração'
        operação = (valor_1 - valor_2)
        sleep(0.5)
        print(f'O valor da {tipo} entre {valor_1} e {valor_2} é igual a {operação}. ')
    elif opção == 3:
        tipo = 'Multiplicação'
        operação = (valor_1 * valor_2)
        sleep(0.5)
        print(f'O valor da {tipo} entre {valor_1} e {valor_2} é igual a {operação}. ')
    else:
        tipo = 'Divisão'
        operação = (valor_1 / valor_2)
        sleep(0.5)
        print(f'O valor da {tipo} entre {valor_1} e {valor_2} é igual a {operação}. ')
print('-=' * 20)
print('=' * 60)
