# Questão 4 da atividade Listas em Python
# Autor: Guilherme Guimarães dos Santos
# Data: 20/07/2022

numeros = list()
cont = 0
n_par = 0
while True:
    num = int(input('Digite um número (-1 encerra o programa): '))
    if num % 2 == 0:
        n_par += 1
    if num != -1:
        numeros.append(num)
    elif num == -1:
        if cont == 0:
            print('Nenhum número foi cadastrado!')
        break
    cont += 1
if len(numeros) > 0: 
    print(f'Foram digitados {n_par} números pares! ')
