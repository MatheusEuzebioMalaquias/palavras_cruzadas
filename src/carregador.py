import json
from pathlib import Path

PASTA_RAIZ = Path(__file__).resolve().parent.parent
PASTA_CONTEUDO = PASTA_RAIZ / "dados" / "conteudo"


def carregar_dados():
    topicos = {}

    for arquivo in sorted(PASTA_CONTEUDO.rglob("*.json")):
        with open(arquivo, encoding="utf-8") as f:
            assunto = json.load(f)

        topicos.setdefault(assunto["topico"], []).append(
            {"nome": assunto["assunto"], "fases": assunto["fases"]}
        )

    return {
        "topicos": [
            {"nome": nome, "assuntos": assuntos}
            for nome, assuntos in topicos.items()
        ]
    }


def carregar_grade(nome_arquivo):
    caminho = PASTA_RAIZ / "dados" / nome_arquivo
    with open(caminho, encoding="utf-8") as arquivo:
        return json.load(arquivo)