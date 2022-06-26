### CATETOS E HIPOTENUSA (IMPORTANDO MATH)###

# Importações
import math

# Strings

cateto_oposto = float(
    input("Digite aqui o valor do cateto oposto em metros: "))
cateto_adjacente = float(
    input("Agora digite o valor do cateto adjacente em metros: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

# Ação - Print
print(f"A hipotenusa mede {hipotenusa} metros.")
