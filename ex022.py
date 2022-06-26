### ANALISADOR DE TEXTOS ###

# Strings ===> Essa função .strip() elimina os espaços vazios antes e depois da str
nome = str(input("\nDigite aqui o seu nome completo: ")).strip()
fragmento = nome.split()

# Ações - Prints

print("\nAnalisando o seu nome...")
print(f"\nSeu nome completo em maíusculas é: {nome.upper()}")
print(f"Seu nome completo em minúsculas é: {nome.lower()}")

# subtraindo o nome.count(' ') eu tiro os espaços da contagem de caractéres
print(f"Seu nome tem ao todo: {len(nome) - nome.count(' ')} letras")

# usando o .find dessa maneira, ele para de contar assim que encontra o primeiro espaço (sem incluí-lo na contagem)
print(
    f"Seu primeiro nome é: {fragmento[0]} e tem {nome.find(' ')} letras. Poderia dizer que ele tem {len(fragmento[0])} letras assim também.\n")
