from src.carregador import carregar_dados
from src.regras import resposta_correta
from src.visual import montar_casas

MAX_TENTATIVAS = 3

dados = carregar_dados()
topico = dados["topicos"][0]
assunto = topico["assuntos"][0]
fase = assunto["fases"][0]

pontos = 0

print("=" * 40)
print("Tópico:", topico["nome"])
print("Assunto:", assunto["nome"])
print("Fase:", fase["numero"])
print("=" * 40)

for palavra in fase["palavras"]:
    print()
    print("Dica:", palavra["dica"])
    print(montar_casas(palavra["resposta"]))

    acertou = False

    for tentativa_atual in range(1, MAX_TENTATIVAS + 1):
        tentativa = input(f"Tentativa {tentativa_atual}/{MAX_TENTATIVAS}: ")

        if resposta_correta(tentativa, palavra["resposta"]):
            acertou = True
            break

        print("Errou!")

    print(montar_casas(palavra["resposta"], revelada=True))

    if acertou:
        print("Acertou! +10 pontos")
        pontos += 10
    else:
        print("Suas tentativas acabaram.")

print()
print("Fim da fase! Pontuação:", pontos)