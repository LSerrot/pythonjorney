### RADAR ELETRÔNICO ### USO DA LIB COLORAMA PARA MUDAR A COR DOS TEXTOS NO PROMPT ###

# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar a velocidade de 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

# Importações
import colorama
from colorama import Fore, Style
colorama.init()

# Strings
v = int(input("\nQual é a velocidade do automóvel?\n"))
multa = (v - 80) * 7

# Ação => Print + If/Else + Format
if v <= 80:
    print(Fore.GREEN + "\nFaça uma boa viagem e dirija com segurança!\n")
else:
    print(Fore.RED + Style.BRIGHT +
          f"\nVocê está trafegando além do limite de 80 km/h e por isso precisará pagar uma multa no valor de R${multa:.2f}.\nFaça isso o quanto antes para não ter a sua CNH cancelada.\n")
input(Fore.RESET + "Aperte 'Enter' para encerrar a sessão.")
