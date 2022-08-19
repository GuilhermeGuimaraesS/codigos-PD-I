# Questão 4 da atividade introdução a Python
# Autor: Guilherme Guimarães dos Santos
# Data: 18/06/2022

print('*' * 60)
print(f'{"CÁLCULO DE GRANDEZAS ELÉTRICAS":^60}')
print('''Digite 
1 - Para Tensão (Volt)
2 - Para Corrente (Ampére)
3 - Para Resistência (Ohm)
''')
print('*' * 60)

opção = 0
opção = int(input('Qual Grandeza deseja calcular? '))
if opção == 1:
    i = float(input('Digite o valor da corrente: ')) 
    r = float(input('Digite o valor da resistência: '))
    u = r * i
    print(f'A Tensão vale {u} Volts. ')
elif opção == 2: 
    u = float(input('Digite o valor da tensão: '))
    r = float(input('Digite o valor da resistência: '))
    i = u / r
    print(f'A Corrente Elétrica vale {i} ampére. ')
elif opção == 3:
    u = float(input('Digite o valor da tensão: '))
    i = float(input('Digite o valor da corrente: '))
    r = u / i
    print(f'A Resistência vale {r} ohms. ')
print('*' * 60)
