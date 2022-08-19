# Questão 1 da atividade introdução a Python
# Autor: Guilherme Guimarães dos Santos
# Data: 14/06/2022
from time import sleep

print(f'{" CÁLCULO DE IMC ":=^30}')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = (peso / (altura**2))

print('-=' * 25)
print(f'Índice de Massa Corporal igual a: {imc:.2f} ')
sleep(1)
print('Situação: ', end='')

if imc < 18.5:
    print('Abaixo do Peso! ')
elif (18.5 <= imc < 25):
    print('Peso normal! ')
elif (25 <= imc < 30):
    print('Sobrepeso! ')
elif imc >= 30:
    if imc < 35:
        print('Obesidade Grau 1! ')
    elif (35 <= imc < 40):
        print('Obesidade Grau 2! ')
    elif imc >= 40:
        print('Obesidade Grau 3! ')
print('-=' * 25)
