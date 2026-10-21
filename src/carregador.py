import json
from pathlib import Path 

PASTA_RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_FASES = PASTA_RAIZ / "dados" / "fases.json"


def carregar_dados():
    with open(ARQUIVO_FASES, encoding="utf-8") as arquivo:
        return json.load(arquivo)
    
def carregar_grade(nome_arquivo):
    caminho = PASTA_RAIZ / "dados" / nome_arquivo
    with open(caminho, encoding="utf-8") as arquivo:
        return json.load(arquivo)