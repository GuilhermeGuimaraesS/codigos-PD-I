# Questão 2 da atividade introdução a Python
# Autor: Guilherme Guimarães dos Santos
# Data: 07/07/2022

print(f'{" CONSULTA DE CREDIÁRIO ":=^50}')
num_conta = -2
while True:
    while num_conta < -1 and num_conta < 0:
        num_conta = int(input('Informe o número da conta (-1 para encerrar): '))
    if num_conta == -1:
        break
    saldo_inicio = float(input('Saldo do mês: '))
    tot_encargos = float(input('Total de encargos: '))
    credito_disp = float(input('Total de crédito disponível: '))
    lim_credito = float(input('Limite de crédito autorizado: '))

    novo_saldo = (saldo_inicio + tot_encargos) - credito_disp
    if novo_saldo > lim_credito:
        print(f'''Conta: {num_conta}
Limite de crédito: {lim_credito:.2f}
Saldo: {novo_saldo:.2f} ''')
        print('Limite de crédito ultrapassado! ')
        print('-' * 50)
    num_conta = -2
print('=' *50)
