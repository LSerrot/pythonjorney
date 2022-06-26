### PPROGRAMA GERADOR DE PROGRESSÃO ARITMÉTICA APRIMORADA ###

# Melhore o ex061, perguntando para o usuário se ele quer mostrar mais alguns termos (e quantos). 
# O programa encerra quando ele disse que quer mostrar 0 termos a mais.

## Strings de input:

print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
contador = 1
total = 0
mais = int(input("Digite quantos ciclos você quer ver nesta PA: "))

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f"{termo} -> ", end = "")
        termo += razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("FIM")