idade = int(input('Idade: '))
peso =  float(input('Peso (Kg): '))
 
grupo_risco = 0

# bloco que analisa o grupo de risco para as pessoas com mais de 50 anos
if idade > 50:
    if peso > 90:
        grupo_risco = 1
    elif peso <= 90 and peso >= 60:
        grupo_risco = 2
    else:
        grupo_risco = 3

# bloco que analisa o grupo de risco para as pessoas de 20 até 50 anos 
elif idade >= 20 and idade <= 50:
    if peso > 90:
        grupo_risco = 4
    if peso <= 90 and peso >= 60:
        grupo_risco = 5
    elif peso < 60:
        grupo_risco = 6

# bloco que analisa o grupo de risco para as pessoas com menos de 20 anos
elif idade < 20:
    if peso > 90:
        grupo_risco = 7
    elif peso <= 90 and peso >= 60:
        grupo_risco = 8
    elif peso < 60:
        grupo_risco = 9

print(f'Essa pessoa pertence ao grupo: {grupo_risco}')
