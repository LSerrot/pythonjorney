### DISSECANDO UMA VARIÁVEL ###

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele:

a = input("Digite algo: ")

# class = str
print(f"O tipo primitivo desse valor é {type(a)}")

# .isspace
print("Só tem espaço vazio?", a.isspace())

# . isnumeric
print("É um número? ", a.isnumeric())

# .isaplha
print("É alfabético? ", a.isalpha())

# .isalnum
print("É alfanumérico? ", a.isalnum())

# .isupper
print("É tudo maiúsculo? ", a.isupper())

# .islower
print("É tudo minúsculo? ", a.islower())

# .istitle
print("Está capitalizada? ", a.istitle())
