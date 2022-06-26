# PROCURANDO UMA STRING DENTRO DE OUTRA ### UTILIZANDO O OPERADOR >>IN<<

# Crie um programa que saiba se o cara tem o nome SILVA dentro do nome dele

# String
# Sem o .splI() um nome como 'Silvana' constaria como 'True'. Divindo com o .split() o problema acaba.
nome = str(input("Qual é o seu nome completo? ")).strip().lower().split()
print("Seu nome tem Silva? {}".format("silva" in nome))
