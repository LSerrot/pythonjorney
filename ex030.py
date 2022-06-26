### PAR OU ÍMPAR ###

# Crie um programa que você dá um número pra ele e ele te diz se é par ou se é ímpar

# Strings
num = int(input("\nDigite um número que eu te digo se é par ou ímpar: "))

# Ação - Print e If

if num % 2 == 0:
    print(f"\n{num} é par!\n")
else:
    print(f"\n{num} é ímpar!\n")
