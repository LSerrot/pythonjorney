### MAIOR E MENOR VALOR ### VERSÃO BURRA, MAS FUNCIONAL ###


# Strings
valor1 = int(input("\nDigite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

lista = [valor1, valor2, valor3]

# Ação

# QUANDO TODOS OS VALORES SÃO DIFERENTES #
if valor1 > valor2 and valor1 > valor3 and valor2 > valor3:
    print(f"\nValor 1: {valor1},\nValor 2: {valor2},\nValor 3: {valor3}\n")

elif valor1 > valor2 and valor1 > valor3 and valor3 > valor2:
    print(f"\nValor 1: {valor1},\nValor 3: {valor3},\nValor 2: {valor2}\n")

elif valor2 > valor1 and valor2 > valor3 and valor1 > valor3:
    print(f"\nValor 2: {valor2},\nValor 1: {valor1},\nValor 3: {valor3}\n")

elif valor2 > valor1 and valor2 > valor3 and valor3 > valor1:
    print(f"\nValor 2: {valor2},\nValor 3: {valor3},\nValor 1: {valor1}\n")

elif valor3 > valor2 and valor3 > valor1 and valor2 > valor1:
    print(f"\nValor 3: {valor3},\nValor 2: {valor2},\nValor 1: {valor1}\n")

elif valor3 > valor2 and valor3 > valor1 and valor1 > valor2:
    print(f"\nValor 3: {valor3},\nValor 1: {valor1},\nValor 2: {valor2}\n")

# QUANDO 2 VALORES SÃO IGUAIS #
elif valor1 > valor2 and valor1 > valor3 and valor2 == valor3:
    print(f"\nValor 1: {valor1},\nValor 2: {valor2},\nValor 3: {valor3}\n")

elif valor2 > valor1 and valor2 > valor3 and valor1 == valor3:
    print(f"\nValor 2: {valor2},\nValor 1: {valor1},\nValor 3: {valor3}\n")

elif valor3 > valor1 and valor3 > valor2 and valor1 == valor2:
    print(f"\nValor 3: {valor3},\nValor 1: {valor1},\nValor 2: {valor2}\n")

elif valor1 < valor2 and valor1 == valor3:
    print(f"\nValor 1: {valor1},\nValor 3: {valor3},\nValor 2: {valor2}\n")

elif valor2 < valor3 and valor1 == valor3:
    print(f"\nValor 1: {valor1},\nValor 3: {valor3},\nValor 2: {valor2}\n")

elif valor1 == valor2 and valor1 > valor3:
    print(f"\nValor 1: {valor1},\nValor 2: {valor2},\nValor 3: {valor3}\n")

elif valor2 == valor3 and valor1 < valor2:
    print(f"\nValor 2: {valor2},\nValor 3: {valor3},\nValor 1: {valor1}\n")

# QUANDO OS 3 VALORES SÃO IGUAIS #
elif valor3 == valor1 and valor3 == valor2 and valor1 == valor2:
    print(f"\nValor 1: {valor1},\nValor 2: {valor2},\nValor 3: {valor3}\n")

print("Digite 'Enter' para encerrar a sessão.")
