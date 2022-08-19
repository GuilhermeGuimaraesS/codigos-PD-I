# Questão 1 da atividade Funções
# Autor: Guilherme Guimarães dos Santos
# Data: 27/07/2022

from time import sleep

# Função que separa os dígitos e os guarda em uma lista
def Separa_Digitos(a):
    global lista
    lista = [0] * 5
    for elemento in range(5):
        lista[elemento] = a % 10
        a = a // 10
    return lista

# Função que compara os algarismos do número digitado com os números contidos em outra lista e retorna quantos são iguais 
def Digitos_Iguais(a, b):
    total_iguais = 0
    for elemento in a:
        for item in b:
            if elemento == item:
                total_iguais += 1
    return total_iguais

# Função que compara as posições dos algarismos do número digitado, que são iguais com a dos contidos na lista do programa
def Posicoes_Iguais(a, b):
    total_mesma_pos = 0
    for elemento in a:
        for pos, item in enumerate(b):
            if elemento == item:
                if a.index(elemento) == pos:
                    total_mesma_pos += 1
    return total_mesma_pos

num = int(input('Digite um número com até 5 digitos: '))
sleep(1)
print('=-' * 30)
print(f'Lista na ordem inversa: {Separa_Digitos(num)} ' )
lista.reverse()
print(f'Lista na ordem correta: {lista} ')
print('=-' * 30)
lista_2 = [9, 5, 2, 1, 8]
sleep(1)
print(f'Comparando o número digitado com a seguinte lista {lista_2}: ')
print(f'Quantidade de digitos iguais: {Digitos_Iguais(lista, lista_2)} ')
print(f'Quantidade de digitos iguais e na mesma posição: {Posicoes_Iguais(lista, lista_2)}')
print('=-' * 30)
