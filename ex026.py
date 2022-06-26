### PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING ###


# Strings

frase = str(input("\nDigite aqui a frase que você quer analisar: ")
            ).strip().lower()
a_count = frase.count('a')
a_position = frase.find('a')
# REVERSE FIND => Procura da direita para a esquerda.
a_positionrev = frase.rfind('a')

# Ação - Print

print(f"\nA letra A aparece {a_count} vezes!")
print(f"A primeira letra A apareceu na posição {a_position + 1}.")
print(f"A última letra A apareceu na posição {a_positionrev + 1}.")
print(
    f"Se ignorarmos os espaços, a última letra A apareceu na posição {(a_positionrev + 1) - frase.count(' ')}.\n")
