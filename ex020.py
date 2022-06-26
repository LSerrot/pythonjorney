### SORTEIO DA ORDEM DE UMA LISTA ### USANDO SHUFFLE DA LIB RANDOM ###

# Importações
from random import shuffle

# Strings
n1 = input("Digite aqui o nome da primeira pessoa: ")
n2 = input("Digite aqui o nome da segunda pessoa: ")
n3 = input("Digite aqui o nome da terceia pessoa: ")
n4 = input("Digite aqui o nome da quarta pessoa: ")
lista = [n1, n2, n3, n4]
shuffle(lista) # O shuffle entra embaixo da lista e não como uma string...

# Ação - Sorteio dentro da lista
print(f"Os selecionados foram {lista}, respectivamente.")
