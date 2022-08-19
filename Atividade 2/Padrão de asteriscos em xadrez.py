# Questão 8 da atividade introdução a Python
# Autor: Guilherme Guimarães dos Santos
# Data: 09/07/2022

print()
cont = 0
while cont <= 8:
    cont += 1
    if cont % 2 == 1:
        print('* ' * 8)
    elif cont % 2 == 0:
        print(f' {"* " * 8}')
    