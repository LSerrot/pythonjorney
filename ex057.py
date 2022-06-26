### VALIDAÇÃO DE DADOS ### USANDO WHILE PELA PRIMEIRA VEZ

sexo = str(input("Informe o seu sexo: [M/F]")).strip().lower()[0]
while sexo not in 'mf':
    sexo = str(input("Dados inválidos. Por favor, informe o seu sexo: [M/F]")).strip().lower()[0]

print("Sexo {} registrado com sucesso".format(sexo))