### CALCULADORA DE TINTA DE PAREDE ###
# Para cada 2 metros quadrados de parede, precisa de 1 litro de tinta.

# Strings
altura = float(input("Digite aqui a altura da sua parede em metros: "))
largura = float(input("Digite aqui a largura da sua parede em metros: "))
area = altura * largura
qtd_tinta = area / 2
galao = 16  # litros

# Print + Format
print(
    f"Sua parede tem a dimensão de {altura} x {largura} e sua área total é de {area:.2f}m².\nPara pintar essa parede, você vai precisar de {qtd_tinta:.2f}l de tinta.\nIsso dá aproximadamente {qtd_tinta/galao:.2f} lata(s).\nBoa sorte!")
