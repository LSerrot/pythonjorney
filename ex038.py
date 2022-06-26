### COMPARADOR ENTRE DOIS NÚMEROS ###

# Strings inputáveis
n1 = int(input("\nDigite aqui o primeiro valor: "))
n2 = int(input("Digite aqui o segundo valor: "))

# Ação - if + print + operações matemáticas básicas
if n1 > n2:
    print("\nO primeiro número É MAIOR que o segundo.")
elif n1 == n2:
    print("\nAmbos os números têm o mesmo valor.")
else:
    print("\nO primeiro número É MENOR que o segundo.")

input("\nDigite 'Enter' para encerrar a sessão. ")
