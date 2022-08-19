numeros = list()

# Esse bloco faz a leitura dos números digitados pelo usuários e guarda eles em uma lista
for c in range(0, 10):
    num = float(input(f'Digite o {c+1}º número: '))
    numeros.append(num)

numeros.sort() # Ordena os números da lista em ordem crescente
print(f'Os números digitados, em ordem crescente foram: {numeros}')
