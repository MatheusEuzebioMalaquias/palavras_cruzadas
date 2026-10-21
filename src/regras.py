import unicodedata

def normalizar(texto):
    decomposto = unicodedata.normalize("NFD", texto)
    sem_acento = "".join(c for c in decomposto if unicodedata.category(c) != "Mn")
    return sem_acento.upper().strip()


def resposta_correta(tentativa, resposta):
    return normalizar(tentativa) == normalizar(resposta)