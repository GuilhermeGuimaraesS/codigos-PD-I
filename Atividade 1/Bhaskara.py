# Questão 3 da atividade introdução a Python
# Autor: Guilherme Guimarães dos Santos
# Data: 17/06/2022
from time import sleep

print('-=' * 40)
print(f'{"RESOLVENDO EQs. DO 2º GRAU":^80}')
print('-=' * 40)
a = float(input('Digite o coeficiente "a" da equação: '))
if a < 0:
    sleep(1)
    print('ERRO! O coeficiente "a" é menor que zero, portanto não é uma equação do 2º grau. ')
else:
    b = float(input('Digite o coeficiente "b" da equação: '))
    c = float(input('Digite o coeficiente "c" da equação: '))
    delta = (b ** 2) - 4 * a * c
sleep(1)
print('-' * 80)
if delta < 0:
    print(f'''Para essa equação, o delta vale {delta} e é menor que 0. 
Portanto, não existe ráiz real para essa equação. ''')
elif delta == 0:
    x = (-b + (delta ** (1/2))) / (2 * a)
    print(f'''Para essa equação, o delta = 0.
Portanto, ela possui uma única raíz real, igual a: {x}''')
elif delta > 0:
    x1 = (-b + (delta ** (1/2))) / (2 * a)
    x2 = (-b - (delta ** (1/2))) / (2 * a)
    print(f'''Para essa equação, o delta vale {delta} e é maior que 0.
Portanto, temos duas raízes reais e distintas, iguais a: {x1} e {x2}. ''')
print('-' * 80)
