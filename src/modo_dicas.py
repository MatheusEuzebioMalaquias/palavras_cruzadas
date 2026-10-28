import random

from src.jogo import MAX_TENTATIVAS, PONTOS_POR_PALAVRA
from src.regras import resposta_correta
from src.visual import montar_casas


def jogar_fase(palavras):
    pontos = 0
    erradas = []

    ordem = list(palavras)
    random.shuffle(ordem)

    for numero, palavra in enumerate(ordem, start=1):
        print()
        print(f"Palavra {numero}/{len(ordem)}")
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
            print(f"Acertou! +{PONTOS_POR_PALAVRA} pontos")
            pontos += PONTOS_POR_PALAVRA
        else:
            print("Suas tentativas acabaram.")
            erradas.append(palavra)

    return pontos, erradas