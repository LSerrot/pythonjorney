# PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA ### USAR LIST[-1] PARA BUSCAR O ÚLTIMO ELEMENTO DE UMA LISTA.

# Crie um programa que separe o seu primeiro e último nome e diga qual é qual logo após você digitá-lo por completo.

# Strings
nome = str(input("\nDigite aqui o seu nome por completo: ")
           ).capitalize().strip().split()

# Ação - Print
print(
    f"\nO seu primeiro nome é {nome[0]},\no seu último nome é {nome[-1].capitalize()}.\n")
