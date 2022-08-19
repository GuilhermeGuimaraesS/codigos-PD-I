# Questão 6 da atividade Listas em Python
# Autor: Guilherme Guimarães dos Santos
# Data: 20/07/2022


numeros_1 = []
numeros_2 = []
numeros_3 = []
cont = 0

print('-=' * 25)
while True:
    num = int(input('Lista 1; Digite um número: (-1 encerra o programa) '))
    if num == -1:
        break
    elif num != -1:
        numeros_1.append(num)
print('-=' * 25)
while True:
    num = int(input('Lista 2; Digite um número: (-1 encerra o programa) '))
    if num == -1:
        break
    elif num != -1:
        numeros_2.append(num)
print('-=' * 25)

numeros_3 = numeros_1.copy()
numeros_3 += numeros_2.copy()
print(f'Os números digitados foram: {numeros_3}')
