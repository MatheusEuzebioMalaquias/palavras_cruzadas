import json

from src.carregador import PASTA_RAIZ

ARQUIVO_PROGRESSO = PASTA_RAIZ / "progresso.json"


def carregar_progresso():
    if not ARQUIVO_PROGRESSO.exists():
        return {}
    with open(ARQUIVO_PROGRESSO, encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_progresso(progresso):
    with open(ARQUIVO_PROGRESSO, "w", encoding="utf-8") as arquivo:
        json.dump(progresso, arquivo, ensure_ascii=False, indent=2)