# Questão 3 da atividade Listas em Python
# Autor: Guilherme Guimarães dos Santos
# Data: 20/07/2022

playlist = []
cont = 0

while True:
    nome_musica = str(input('Digite o nome da música que você quer adicionar: ("FIM" encerra o programa )')).upper()

    if nome_musica != 'FIM':
        playlist.append(nome_musica)
    elif nome_musica == 'FIM':
        if cont == 0:
            print('Nenhuma música foi registrada!')
        break
    cont += 1
if len(playlist) > 0:
    print(f'As músicas digitadas foram: {playlist}')
