# Questão 5 da atividade introdução a Python
# Autor: Guilherme Guimarães dos Santos
# Data: 09/07/2022

print('='*30)
print('Num','\t10*N','\t100*N','\t1000*N')
print('='*30)
cont = 0
while True:
    cont += 1
    if cont > 10:
        break
    print(f'{cont}', f'\t{cont*10}', f'\t{cont*100}', f'\t{cont*1000}')
    