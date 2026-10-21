def criar_quadro(linhas, colunas):
    return [[None for _ in range(colunas)] for _ in range(linhas)]


def posicoes_da_palavra(palavra):
    posicoes = []
    for indice, letra in enumerate(palavra["resposta"]):
        if palavra["direcao"] == "horizontal":
            linha = palavra["linha"]
            coluna = palavra["coluna"] + indice
        else:
            linha = palavra["linha"] + indice
            coluna = palavra["coluna"]
        posicoes.append((linha, coluna, letra))
    return posicoes


def montar_quadro(dados_grade):
    quadro = criar_quadro(dados_grade["linhas"], dados_grade["colunas"])

    for palavra in dados_grade["palavras"]:
        for linha, coluna, letra in posicoes_da_palavra(palavra):
            if linha >= dados_grade["linhas"] or coluna >= dados_grade["colunas"]:
                raise ValueError(f"{palavra['resposta']} não cabe no quadro")

            atual = quadro[linha][coluna]
            if atual is not None and atual != letra:
                raise ValueError(
                    f"Conflito em ({linha}, {coluna}): "
                    f"'{atual}' x '{letra}' na palavra {palavra['resposta']}"
                )

            quadro[linha][coluna] = letra

    return quadro