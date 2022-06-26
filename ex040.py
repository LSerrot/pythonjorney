### BOLETIM ###

# Criar um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0 => REPROVADO
# - Média entre 5.0 e 6.9 => RECUPERAÇÃO
# - Média 7.0 ou superior => APROVADO

# Strings inputáveis
nota1 = float(input("\nDigite aqui a nota da P1: "))
nota2 = float(input("Digite aqui a nota da P2: "))
nota3 = float(input("Digite aqui a nota da P3: "))
nota4 = float(input("Digite aqui a nota da P4: "))

# Strings de cálculos
media = (nota1 + nota2 + nota3 + nota4) / 4

# Ações - if + print + format
if media < 5:
    print(
        f"\nSua média é {media}. Ela está {5 - media} ponto(s) abaixo da média, que é 5. Você está REPROVADO!")
elif 6.9 >= media >= 5:
    print(
        f"\nSua média é {media}. Você está entre os 5 e os 6,9 pontos. Isso te faz de RECUPERAÇÃO!")
else:
    print(
        f"\nVocê está com {media}, ou seja, {media - 7} ponto(s) acima da média. Você está APROVADO!")

# Input de encerramento
input("\nDigite 'Enter' para fechar a sessão. ")
