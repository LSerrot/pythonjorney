### PPROGRAMA GERADOR DE PROGRESSÃO ARITMÉTICA ###

## Strings de input:

n = int(input("Digite aqui o primeiro termo: "))
r = int(input("Digite aqui a razão: "))
termo = n
contador = 1
tamanho = 12500


## Ação => while + if/else inline + end ="" + operações matemáticas de maior e menor

while contador <= tamanho: # Enquanto o contador estiver menor ou igual a 'tamanho' (vamos dizer 10)
    print(f"{termo} + " if contador < tamanho else f"{termo} ", end = "") # o end="" aqui horizontaliza o processo, 
    # mas deve ser observado que a linha abaixo se mescla com essa antes dessa linha repetir o processo dela novamente.
    print(f"{r} = " if contador < tamanho else "=> FIM", end = "") # fica como se fosse: |linha 1 + linha 2 | linha 1 + linha 2 | linha 1 + linha 2 | ...
    termo += r # A cada repetição dentro do ciclo do 'while' o termo é acrescido da razão R, 
    # atualizando-se enquanto a razão permanece constante e constantemente sendo acrescida ao novo termo.
    contador += 1 # A cada novo ciclo do 'while' o contador é acrescido de 1, crescendo assim até chegar no seu limite ('tamanho') e interromper o ciclo do 'while'.