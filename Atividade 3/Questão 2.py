# Questão 2 da atividade Listas em Python
# Autor: Guilherme Guimarães dos Santos
# Data: 20/07/2022

numeros = []
cont = 0
while True: 
    num = int(input('Digite um número: (-1 Encerra o programa) '))
    if num != -1:
        numeros.append(num)
    elif num == -1:
        if cont == 0:
            print('Nenhum número foi digitado. ')
        break
    cont += 1
if len(numeros) > 0:
    print(f'Os números digitados foram: {numeros[::-1]}')
