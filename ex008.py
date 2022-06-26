### CONVERSOR DE MEDIDAS DE DISTÂNCIAS ###

# String
metros = float(input("Digite aqui a distância em metros: "))

milimetros = metros * 1000
centimetros = metros * 100
decimetros = metros * 10
decametros = metros / 10
hectometros = metros / 100
kilometros = metros / 1000

# Print + format
print(f"A medida de {metros} corresponde a \n{milimetros:.0f} milímetros, \n{centimetros:.0f} centímetros, \n{decimetros:.0f} decimetros, \n{decametros} decametros, \n{hectometros} hectometros,\n{kilometros} kilometros.")