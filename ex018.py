### SENO, COSSENO E TANGENTE ###

# Importações ===> Usando 'FROM' e 'IMPORT' para deixar as linhas bem limpas, sem ter que toda hora ficar aludindo à libraria 'MATH' antes de cada importação pontual.
from math import radians, sin, cos, tan

# Strings
angulo = float(input("\nDigite o ângulo: "))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

# Ação - Print
print(
    f"\nO ângulo {angulo} tem as seguinte medidas de SENO, COSSENO e TANGENTE:")
print(f"SENO: {sen :.2f}")
print(f"COSSENO: {cos :.2f}")
print("TANGENTE: {:.2f}\n".format(tan))
