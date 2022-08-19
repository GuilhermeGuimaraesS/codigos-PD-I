# Questão 5 da atividade Listas em Python
# Autor: Guilherme Guimarães dos Santos
# Data: 20/07/2022

numeros = []
cont = 0
while True:
    num = int(input('Digite um número: (-1 encerra o programa) '))
    if num == -1:
        if cont == 0:
            print('Nenhum número foi registrado! ')
        break
    if num != -1:
        numeros.append(num)
    cont += 1
    
if len(numeros) > 0:
    maior_valor = max(numeros)
    menor_valor = min(numeros)
    print(f'O maior valor da lista é {maior_valor}. E o menor valor da lista é {menor_valor}! ')
