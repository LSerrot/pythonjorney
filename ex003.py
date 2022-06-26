### CALCULADORA DAS QUATRO OPERAÇÔES ###

##################################################################################################################

# STRINGS #

operação = input(
    "Digite a operação que você deseja realizar: 'SOMA', 'SUBTRAÇÃO', 'MULTIPLICAÇÃO' ou 'DIVISÃO'. => ").lower()
valor1 = int(input("Digite aqui o primeiro número: "))
valor2 = int(input("Digite aqui o segundo número: "))
soma = valor1 + valor2
subtração = valor1 - valor2
multiplicação = valor1 * valor2
divisão = valor1 / valor2

#################################################################################################################

# FUNCTIONS #

if operação == 'soma':
    print(f"O resultado da soma entre {valor1} e {valor2} é {soma}!")

elif operação == 'subtração':
    print(f"O resultado da subtração entre {valor1} e {valor2} é {subtração}!")

elif operação == 'multiplicação':
    print(
        f"O resultado da multiplicação entre {valor1} e {valor2} é {multiplicação}!")

elif operação == 'divisão':
    print(f"O resultado da divisão entre {valor1} e {valor2} é {divisão}!")

input("Aperte 'Enter' para encerrar a sessão.")
