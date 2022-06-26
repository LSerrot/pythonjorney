### CALCULADORA DE DOBRO, TRIPLO E RAIZ QUADRADA ###

# Inputs
operação = input(
    "Digite aqui a operação que você deseja efetuar: 'DOBRO', 'TRIPLO' ou 'RAIZ QUADRADA' => ").lower()
numero = float(input("Digite o número aqui: "))

# Resultados
dobro = numero * 2
triplo = numero * 3
raiz2 = numero ** (1/2) # ou raiz2 = pow(numero, (1/2))

# Funções
if operação == "dobro":
    print(f"O dobro de {numero} vale {dobro}")

elif operação == 'triplo':

    print(f"O triplo de {numero} vale {triplo}")

elif operação == 'raiz quadrada' or 'raíz quadrada':
    print(f"A raíz quadrada de {numero} é {raiz2:.2f}")
    # ===>  ':.(x)f' onde (x) = número de casas decimais desejadas

input("Aperte 'Enter' para encerrar a sessão.")
