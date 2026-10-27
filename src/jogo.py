from src.grade import montar_quadro, posicoes_da_palavra
from src.regras import resposta_correta
from src.visual import desenhar_quadro

MAX_TENTATIVAS = 3
PONTOS_POR_PALAVRA = 10


def jogar_grade(dados_grade):
    quadro = montar_quadro(dados_grade)
    palavras = dados_grade["palavras"]

    reveladas = set()
    resolvidas = set()
    pontos = 0

    while len(resolvidas) < len(palavras):
        print()
        desenhar_quadro(quadro, reveladas)
        print()

        for numero, palavra in enumerate(palavras, start=1):
            marca = "X" if numero in resolvidas else " "
            print(f"{numero}. [{marca}] {palavra['dica']} "
                  f"({len(palavra['resposta'])} letras, {palavra['direcao']})")

        escolha = input("\nNúmero da palavra (0 para sair): ")

        if escolha == "0":
            break

        if not escolha.isdigit() or not 1 <= int(escolha) <= len(palavras):
            print("Número inválido.")
            continue

        numero = int(escolha)

        if numero in resolvidas:
            print("Essa palavra já foi resolvida.")
            continue

        palavra = palavras[numero - 1]
        acertou = False

        for tentativa_atual in range(1, MAX_TENTATIVAS + 1):
            tentativa = input(f"Tentativa {tentativa_atual}/{MAX_TENTATIVAS}: ")

            if resposta_correta(tentativa, palavra["resposta"]):
                acertou = True
                break

            print("Errou!")

        for linha, coluna, _ in posicoes_da_palavra(palavra):
            reveladas.add((linha, coluna))

        resolvidas.add(numero)

        if acertou:
            print(f"Acertou! +{PONTOS_POR_PALAVRA} pontos")
            pontos += PONTOS_POR_PALAVRA
        else:
            print("Suas tentativas acabaram. A palavra foi revelada.")

    print()
    desenhar_quadro(quadro, reveladas)
    return pontos