def montar_casas(resposta, revelada=False):
    if revelada:
        return " ".join(f"[{letra}]" for letra in resposta)
    return " ".join("[ ]" for _ in resposta)


def desenhar_quadro(quadro, reveladas=None, dicas=None):
    for numero_linha, linha in enumerate(quadro):
        casas = []
        for numero_coluna, casa in enumerate(linha):
            posicao = (numero_linha, numero_coluna)
            if casa is not None:
                if reveladas is None or posicao in reveladas:
                    casas.append(f"[{casa}]")
                else:
                    casas.append("[ ]")
            elif dicas is not None and posicao in dicas:
                texto = "/".join(str(n) for n in dicas[posicao])
                casas.append(f"{texto:^3}")
            elif dicas is not None:
                casas.append("###")
            else:
                casas.append(" . ")
        print(" ".join(casas))