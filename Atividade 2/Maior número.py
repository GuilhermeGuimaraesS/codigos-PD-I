# Questão 4 da atividade introdução a Python
# Autor: Guilherme Guimarães dos Santos
# Data: 09/07/2022

cont = 0
maior = 0
while True:
    num = int(input('Digite um número: '))
    if cont == 1:
        maior = num
    else:
        if num > maior:
            maior = num
    if cont == 10:
        break
    cont += 1
    print(f'{cont}º número: {num}')
    print(f'O maior número digitado até o momento foi {maior}. ')
print(f'O maior número entre os digitados foi {maior}. ')
