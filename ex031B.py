### CUSTO DA VIAGEM ### USANDO IF E ELSE HORIZONTALMENTE, DIRETO NA STR ###

'''Desenvolva um programa que pergunte a distância de uma viagem em Km e calcule o preço da passagem,
cobrando R$0,50 por KM para viagens de até 200km e R$0,45 para viagens mais longas.'''

# Strings
viagem = float(input("\nDigita aqui a distância da sua viagem: "))
preco = viagem * 0.5 if viagem <= 200 else viagem *0.45

# Ação - Print e If
print(f"\nO valor da sua passagem será de R${preco:.2f}\n")

print("Digite 'Enter' para finalizar a sessão.\n")

### O IF simplificado não é muito bem recomendado, mas funciona também.