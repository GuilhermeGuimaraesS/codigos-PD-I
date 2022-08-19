from time import sleep

print(f'{" TABUADA ":=^50}')
while True:
    num = int(input('Digite um número (999 para sair): '))
    if num == 999:
        break
    print('-' * 50)
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')
    print('-' * 50)
    sleep(0.5)
print('=' * 50)
print('SAINDO... ')
sleep(1)
