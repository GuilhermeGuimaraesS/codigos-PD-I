# Questão 1 da Terceira avaliação de Python
# Autor: Guilherme Guimarães dos Santos
# Data: 29/07/2022

from random import randint, seed
from time import sleep

def Gerador_Senha(a, b): # a = semente; b = total de dígitos da senha
    seed(a)
    global senha
    if b == 2:
        senha = randint(10, 99)
    elif b == 3:
        senha = randint(100, 999)
    elif b == 4:
        senha = randint(1000, 9999)
    elif b == 5:
        senha = randint(10000, 99999)
    return senha

def Separa_Digitos(a, b):
    global lista
    lista = [0] * b
    for elemento in range(b):
        lista[elemento] = a % 10 # Guarda o ultimo elemento em uma lista
        a = a // 10 # Armazena o número sem o elemento retirado na linha acima
    lista.reverse() # Ordena os números de forma correta
    return lista

def Digitos_Iguais(a, b): # a = lista com palpite do usuário; b = lista com a senha gerada
    total_iguais = 0
    for elemento in a:
        for item in b:
            if elemento == item:
                total_iguais += 1
    return total_iguais

def Posicoes_Iguais(a, b): # a = lista com palpite do usuário; b = lista com a senha gerada
    total_mesma_pos = 0
    for elemento in a:
        for pos, item in enumerate(b):
            if elemento == item and a.index(elemento) == pos:
                total_mesma_pos += 1
    return total_mesma_pos

print('=' * 120)
print('=' * 120)
print(f'{" BEM VINDO AO JOGO ADVINHE A SENHA ":=^120}')
print('=' * 120)
print(f'{" NESSE JOGO VOCÊ TERÁ 5 CHANCES PARA ACERTAR A SENHA DE PODE CONTER DE 2 À 5 DIGITOS ":=<120}')
print(f'{" VOCÊ DEFINIRÁ O TAMANHO DELA ":=<120}')
sleep(0.5)

semente_senha = int(input('Digite uma semente para gerar a senha (se usar a mesma semente e o mesmo total de dígitos, o número gerado será igual): '))
while True:
    tam_senha = int(input('Quantos dígitos você quer na senha? (2 à 5 dígitos) '))
    if tam_senha >= 2 and tam_senha <= 5:
        break
    else:
        print('NÚMERO INVÁLIDO!')

senha_gerada = Gerador_Senha(semente_senha, tam_senha)
lista_1 = Separa_Digitos(senha_gerada, tam_senha)

sleep(0.5)
print('Você terá 5 chances para tentar acertar a senha!')
sleep(0.5)

chances = 0
while chances < 5:    
    palpite_usuario = int(input(f'TENTATIVA {chances + 1}. Digite o seu palpite (com {tam_senha} dígitos)): '))

    lista_2 = Separa_Digitos(palpite_usuario, tam_senha)
    acertos_digitos = Digitos_Iguais(lista_1, lista_2)
    acertos_pos = Posicoes_Iguais(lista_1, lista_2)

    print(f'Dígitos corretos: {acertos_digitos} ')
    print(f'Dígitos em posições corretas: {acertos_pos} ')

    if lista_2 == lista_1:
        print('=' * 120)
        print(f'Parabéns, você acertou em {chances + 1} tentativas! ')
        break
    elif chances == 4 and lista_2 != lista_1:
        print('=' * 120)
        print(f'Você não conseguiu acertar. A senha correta seria {senha}. ')

    acertos_digitos = acertos_pos = 0
    lista_2.clear()
    chances += 1
