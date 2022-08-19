# Questão 1 da atividade Listas em Python
# Autor: Guilherme Guimarães dos Santos
# Data: 20/07/2022

numeros = list()
cont = 0
while cont < 6:
    num = int(input(f'Digite o {cont + 1}º número: '))
    numeros.append(num)
    cont += 1
print(f'Os números digitados foram: {numeros[::-1]}')
