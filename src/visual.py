def montar_casas(resposta, revelada=False):
    if revelada:
        return " ".join(f"[{letra}]" for letra in resposta)
    return " ".join("[ ]" for _ in resposta)

def desenhar_quadro(quadro, reveladas=None):
    for numero_linha, linha in enumerate(quadro):
        casas = []
        for numero_coluna, casa in enumerate(linha):
            if casa is None:
                casas.append(" . ")
            elif reveladas is None or (numero_linha, numero_coluna) in reveladas:
                casas.append(f"[{casa}]")
            else:
                casas.append("[ ]")
        print(" ".join(casas))