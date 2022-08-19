faixa_etaria_1 = faixa_etaria_2 = faixa_etaria_3 = faixa_etaria_4 = faixa_etaria_5 = 0

print('=' * 50)

# Bloco que analisa a idade digitada pelo usuário e aloca na variável correspondente a faixa etária que ela pertence
for cont in range(0, 8):
    idade = int(input(f'Digite a idade da {cont+1}ª pessoa: '))
    if idade <= 15:
        faixa_etaria_1 += 1
    elif idade >= 16 and idade <= 30:
        faixa_etaria_2 += 1
    elif idade >= 31 and idade  <= 45:
        faixa_etaria_3 += 1
    elif idade >= 46 and idade <= 60:
        faixa_etaria_4 += 1
    elif idade > 60:
        faixa_etaria_5 += 1

# Lista com o total de pessoas em cada faixa etária     
total_pessoas_faixa = [faixa_etaria_1, faixa_etaria_2, faixa_etaria_3, faixa_etaria_4, faixa_etaria_5] 

print('=' * 50)
cont = 1
for i in total_pessoas_faixa:
    print(f'Total de pessoas na faixa etária {cont+1}: {i}')
    cont += 1
porc_grupo_1 = (100 * faixa_etaria_1) / 8
print(f'{porc_grupo_1:.1f}% das pessoas estão incluídas na primeira faixa etária. ' )

porc_grupo_5 = (100 * faixa_etaria_5) / 8
print(f'{porc_grupo_5:.1f}% das pessoas estão incluídas na ultima faixa etária. ')
print('=' * 50)
