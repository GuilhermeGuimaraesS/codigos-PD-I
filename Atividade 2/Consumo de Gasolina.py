# Questão 1 da atividade introdução a Python
# Autor: Guilherme Guimarães dos Santos
# Data: 07/07/2022

qntd_combustivel = -2
soma_consumo = 0
consumo_total = 0
cont = 0

while True:
    while qntd_combustivel < -1 and qntd_combustivel < 0:
        qntd_combustivel = float(input('Quantidade de combustível em litros (-1 para terminar): '))
    if qntd_combustivel == -1:
        break
    km_rodados = float(input('Dirigiu por quantos km: '))
    cont += 1
    consumo =  km_rodados / qntd_combustivel
    print(f'O consumo atual é {consumo:.2f} km/l. ')
    soma_consumo += consumo 
    consumo_total = soma_consumo / cont 
    qntd_combustivel = -2
    
print(f'O consumo total de combustível foi de {consumo_total:.2f} km/l. ')
