### ANO BISSEXTO ### IMPORTAÇÃO DA LIB DATETIME PARA CHAMAR A FUNÇÃO DATE E PUXAR A DATA A PARTIR DAS CONFIGURAÇÕES DO PC QUE LÊ O SCRIPT ###

# Importações
from datetime import date

# Strings
ano = int(
    input("\nQue ano quer analisar? Digite [0] para analisar o ano atual: "))

# Ação - Print e Operação
if ano == 0: # ... Se o cara digitar [0]...
    ano = date.today().year 
# o ano vai ser [ano atual]... 
# com o .today() eu chamo o 'hoje' e com o .year eu printo somente o 'ano' atual. 
# Chama-se direto da configuração da máquina

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # *
    print(f"\nO ano {ano} É BISSEXTO.")
else:
    print(f"\nO ano {ano} NÃO É bissexto.")

input("\nDigite 'Enter' para encerrar a sessão.\n")



#############################################

# * No caso de um ano bissexto, ele ocorre 
# a cada 4 anos (ano % 4 == 0), salvo quando é 
# um múltiplo de 100 (and ano % 100 != 0). 
# Contudo, se ele for um múltiplo de 100, porém 
# também for múltiplo de 400, ele ainda assim é 
# um ano bissexto (or ano % 400 == 0)'''