### ALISTAMENTO MILITAR ###

# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele AINDA VAI SE ALISTAR ao serviço militar,
# se É A HORA DE SE ALISTAR, ou se JÁ PASSOU DA HORA DE SE ALISTAR. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Importações
from datetime import date

# Strings inputáveis
nscmnt = int(input("\nDigite o ano do seu nascimento: "))

# Strings de cálculo
idade = date.today().year - nscmnt
falta = 18 - idade
passou = idade - 18
anofuturo = date.today().year + falta
anopassado = date.today().year - passou

# Ações => if + print
print(
    f"\nSe você nasceu em {nscmnt}, nesse ano você completa(ou) {idade} anos.")
if idade == 18:
    print("Você precisa se alistar nesse ano, não perca os seus prazos com o Serviço Militar Brasileiro!")
elif idade < 18:
    # Aproveitei para brincar com a possibilidade de prints diferentes para quando falta somente um ano (e exige um texto singular) e quando falta 2 anos ou mais (e aí o texto acompanha no plural).
    if falta == 1:
        print(
            f"Você deverá se alistar daqui a UM ano, em {anofuturo}. Não se esqueça.")
    else:
        print(
            f"Você deverá se alistar daqui a {falta} anos, em {anofuturo}. Não se esqueça.")
else:
    # Aproveitei para brincar com a possibilidade de prints diferentes para quando falta somente um ano (e exige um texto singular) e quando falta 2 anos ou mais (e aí o texto acompanha no plural).
    if passou == 1:
        print(
            f"Você já era para ter se alistado há um ano, em {anopassado}.\nVá o quanto antes até uma junta militar para regularizar as suas pendências com o Serviço Militar Brasileiro.")
    else:
        print(
            f"Você já era para ter se alistado há {passou} anos, no ano de {anopassado}.\nVá o quanto antes até uma junta militar para regularizar as suas pendências com o Serviço Militar Brasileiro.")

input("\nDigite 'Enter' para encerrar a sessão. ")
