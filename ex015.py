### CALCULADOR DE ALUGUEL DE CARROS ###

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi rentado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

# Strings

dias = int(input("Por quantos dias vocês ficou com o carro? "))
kms = float(input("E quantos kilometros você rodou com ele? "))

# Ação => Print + Format

print(f"\nVocê passou {dias} dias com o carro, o que equivale a R${dias * 60:.2f}.\nAlém disso, foram rodados {kms:.2f} kilometros, o que dá R${kms * 0.15:.2f}.\nSomando tudo isso, o valor total do seu aluguel é de R${(dias * 60) + (kms * 0.15):.2f}.\n")
