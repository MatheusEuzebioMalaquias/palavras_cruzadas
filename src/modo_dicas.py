import random

from src.jogo import MAX_TENTATIVAS, PONTOS_POR_PALAVRA
from src.regras import resposta_correta
from src.visual import montar_casas


def perguntar(palavra):
    print("Dica:", palavra["dica"])
    print(montar_casas(palavra["resposta"]))

    for tentativa_atual in range(1, MAX_TENTATIVAS + 1):
        tentativa = input(f"Tentativa {tentativa_atual}/{MAX_TENTATIVAS}: ")

        if resposta_correta(tentativa, palavra["resposta"]):
            print(montar_casas(palavra["resposta"], revelada=True))
            return True

        print("Errou!")

        dica_extra = palavra.get("dica_extra")
        if tentativa_atual == 1 and dica_extra:
            print("Dica extra:", dica_extra)

    print(montar_casas(palavra["resposta"], revelada=True))
    return False

def jogar_fase(palavras):
    pontos = 0
    erradas = []

    ordem = list(palavras)
    random.shuffle(ordem)

    for numero, palavra in enumerate(ordem, start=1):
        print()
        print(f"Palavra {numero}/{len(ordem)}")

        if perguntar(palavra):
            print(f"Acertou! +{PONTOS_POR_PALAVRA} pontos")
            pontos += PONTOS_POR_PALAVRA
        else:
            print("Suas tentativas acabaram.")
            erradas.append(palavra)

    return pontos, erradas


def revisar(erradas):
    pendentes = list(erradas)
    rodada = 1

    while pendentes:
        print(f"\n--- Revisão: rodada {rodada} ---")
        ainda_erradas = []

        for palavra in pendentes:
            print()
            if not perguntar(palavra):
                ainda_erradas.append(palavra)

        pendentes = ainda_erradas
        rodada += 1

        if pendentes:
            resposta = input(
                f"\nAinda faltam {len(pendentes)} palavra(s). Revisar de novo? (s/n): "
            )
            if resposta.strip().lower() != "s":
                return

    print("\nRevisão concluída! Você acertou todas.")