### CATETOS E HIPOTENUSA ###

# Strings

cateto_oposto = float(
    input("Digite aqui o valor do cateto oposto em metros: "))
cateto_adjacente = float(
    input("Agora digite o valor do cateto adjacente em metros: "))
hipotenusa = (cateto_oposto**2 + cateto_adjacente**2) ** (1/2)

# Ação - Print (usando o {}.format() ao invés do f{x})
print("A hipotenusa é: {:.2f}".format(hipotenusa))
