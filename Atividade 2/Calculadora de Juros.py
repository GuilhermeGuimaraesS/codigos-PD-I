# Questão 3 da atividade introdução a Python
# Autor: Guilherme Guimarães dos Santos
# Data: 07/07/2022

print(f'{" CALCULANDO JUROS SIMPLES ":=^50}')
valor_emprestimo = -2
while True:
    while valor_emprestimo < -1 and valor_emprestimo < 0:
        valor_emprestimo = float(input('Digite o valor total do empréstimo (-1 para fechar o programa): '))
    if valor_emprestimo == -1:
        break
    tx_juros = float(input('Digite a taxa de juros em %: '))
    tx_juros_f = tx_juros / 100
    prazo_dias = int(input('Digite o prazo do empréstimo (em dias): '))
    juros = (valor_emprestimo * tx_juros_f * prazo_dias) / 365
    print(f'O valor dos juros é R${juros:.2f} ')
    valor_emprestimo = -2
    print('-' * 50)
print('=' * 50)
