# JOGO DA ADIVINHAÇÂO ### USANDO O RANDINT ### IMPORTANDO A LIB TIME

# Importações
from random import randint
from time import sleep

# Strings
# ===> O computador sorteia um número entre x e y, contando com x e y.
n_sort = randint(0, 5)

print()
print("-=-" * 23)
n_input = int(input(
    "Vou pensar em um número de 0 a 5. Tente advinhar e me vencer... => "))
print("-=-" * 23)
# Ações
print("\nProcessando...")

print()
sleep(0.5)
print(".")
sleep(0.5)
print(".")
sleep(0.5)
print(".")
sleep(0.5)
print()

if n_input == n_sort:
    print(f"\nBoa, você pensou igual a mim. {n_sort}!\n")
else:
    print(f"\nVocê errou. Eu pensei no {n_sort}!\n")
