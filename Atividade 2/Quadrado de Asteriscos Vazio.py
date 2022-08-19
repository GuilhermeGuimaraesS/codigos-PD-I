# Questão 7 da atividade introdução a Python
# Autor: Guilherme Guimarães dos Santos
# Data: 09/07/2022

lado_quadrado = int(input('Digite o lado do quadrado (número entre 1 e 20): '))
print()
cont = 0
while cont < lado_quadrado:
    cont += 1 
    if cont == 1 or cont == lado_quadrado:
        print('*' * lado_quadrado)
    else:
        print(f'{"*":<{lado_quadrado-1}}{"*"}')   
