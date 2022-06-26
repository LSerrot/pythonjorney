# DADOS PREENCHIDOS PELO USUÁRIOS:Ann

nome = input("Digite o seu nome: ")
idade = input("Agora digite a sua idade: ")
curso = input(
    "Para qual curso você está se preparando? Exemplo: Medicina, Engenharia Civil, Direito, Matemática etc. ")
universidade = input(
    "E para qual universidade você quer passar? Basta digitar a sigla (exemplo: UFRJ, UFBA, UFRGS etc): ")
enem_quantidade = input(
    "Quantas vezes você já fez o Enem? Digite '0' caso nunca tenha feito.")

# iNTERAÇÃO DO SISTE

print(
    f"Seja muito bem-vinda, {nome}, você certamente conseguirá passar para {curso} na {universidade}.")

if enem_quantidade == "0":
    print(f"Você tem {idade} anos e nunca fez o Enem.")

else:
    print(
        f"Você tem {idade} anos e já fez o Enem {enem_quantidade} vezes. Você vai passar.")