### VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO ###

# Crie um programa que lê o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

# String
cidade = str(input("Digite aqui a sua cidade natal: ")).strip().lower()

# Print
if cidade[:5] == "santo":
    print("Esta cidade começa com o nome SANTO.")
elif (cidade[:5]) == "santa":
    print("Esta cidade começa com o nome SANTA.")
elif cidade[:3] == "são":
    print("Esta cidade começa com o nome SÃO.")
else:
    print("Esta cidade NÃO é uma cidade abençoada.")
