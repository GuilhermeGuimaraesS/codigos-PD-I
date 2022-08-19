from time import sleep

horas_trab = float(input('Digite o número de horas trabalhadas: '))
salario_min = float(input('Digite o valor do salário mínimo: '))
horas_ext = float(input('Total de horas extras trabalhadas: '))

valor_hora = (salario_min / 8)
valor_hora_ext = (salario_min / 4) # valor a receber por cada hora extra
salario_bruto = (horas_trab * valor_hora)
pagamento_ext = (horas_ext * valor_hora_ext) # valor total a receber pelas horas extras trabalhadas
salario_final = (salario_bruto + pagamento_ext)

print('CALCULANDO... ')
sleep(1)
print( f'O salário total desse funcionário será de R$ {salario_final:.2f} ')
