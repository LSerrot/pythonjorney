### SORTEANDO UM TEMA NA LISTA ### UTILIZAÇÂO DO RANDOM PELA PRIMEIRA VEZ - CHOICE ###

# Importações
from random import choice

# Strings
n1 = str(input("Digite o nome do(a) primeiro(a) aluno(a): "))
n2 = str(input("Digite o nome do(a) segundo(a) aluno(a): "))
n3 = str(input("Digite o nome do(a) terceiro(a) aluno(a): "))
n4 = str(input("Digite o nome do(a) quarto(a) aluno(a): "))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)

# Ação - Print
print(f"O(a) aluno(a) escolhido(a) é o(a) {escolhido}!")
