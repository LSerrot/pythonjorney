### CUSTO DA VIAGEM ###

# Desenvolva um programa que pergunte a distância de uma viagem em Km e calcule o preço da passagem,
# cobrando R$0,50 por KM para viagens de até 200km e R$0,45 para viagens mais longas.

# Strings
viagem = float(input("\nDigita aqui a distância da sua viagem: "))
viagem_p = viagem * 0.5
viagem_g = viagem * 0.45

# Ação - Print e If
if viagem > 200:
    print("\nO custo da sua passagem será de R${:.2f}.\n".format(viagem_g))
else:
    print("\nO custo da sua passagem será de R${:.2f}.\n".format(viagem_p))

print("Digite 'Enter' para encerrar a sessão.\n")