### JOGO DA ADIVINHAÇÃO ###

# Importações
from random import choice

# Strings
n = [0, 1, 2, 3, 4, 5]
n_sort = choice(n)
n_input = int(input(
    "\nDigite aqui um número de 0 a 5 e tente descobrir o mesmo que eu estou pensando: "))

# Ações
if n_input == n_sort:
    print(f"\nParabéns, você acertou o mesmo número que eu! ({n_sort})\n")
else:
    print(f"Ganhei! Você escolheu {n_input} e eu pensei no {n_sort}!\n")
