# Questão 7 da atividade Listas em Python
# Autor: Guilherme Guimarães dos Santos
# Data: 20/07/2022

numeros_1 = list()
numeros_2 = list()
numeros_3 = list()

print('-=' * 25)
# Bloco que lê os números digitados pelo usuario e armazena na Lista 1
while True: 
    num = int(input('Lista 1; Digite um número: (-1 encerra o programa) '))
    if num == -1:
        break
    elif num != -1:
        numeros_1.append(num)
print('-=' * 25)
# Bloco que lê os números digitados pelo usuario e armazena na Lista 2
while True: 
    num = int(input('Lista 2; Digite um número: (-1 encerra o programa) '))
    if num == -1:
        break
    elif num != -1:
        numeros_2.append(num)
print('-=' * 25)

# Bloco que analisa as duas listas e adiciona os valores de cada uma na Lista 3, caso um valor igual já tenha sido adicionado o programa ignora
for c in numeros_1:
    if c not in numeros_3:
        numeros_3.append(c)
for c in numeros_2:
    if c not in numeros_3:
        numeros_3.append(c)
    
print(f'Os números digitados (sem as repetições) foram: {numeros_3}')
print('-=' * 25)
