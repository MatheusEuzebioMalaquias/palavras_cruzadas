import json
from pathlib import Path

PASTA_RAIZ = Path(__file__).resolve().parent.parent
PASTA_CONTEUDO = PASTA_RAIZ / "dados" / "conteudo"


def carregar_dados():
    topicos = {}

    for arquivo in sorted(PASTA_CONTEUDO.rglob("*.json")):
        with open(arquivo, encoding="utf-8") as f:
            conteudo = json.load(f)

        assuntos = topicos.setdefault(conteudo["topico"], {})
        fases = assuntos.setdefault(conteudo["assunto"], [])
        fases.extend(conteudo["fases"])

    return {
        "topicos": [
            {
                "nome": nome_topico,
                "assuntos": [
                    {
                        "nome": nome_assunto,
                        "fases": sorted(fases, key=lambda fase: fase["numero"]),
                    }
                    for nome_assunto, fases in assuntos.items()
                ],
            }
            for nome_topico, assuntos in topicos.items()
        ]
    }


def carregar_grade(nome_arquivo):
    caminho = PASTA_RAIZ / "dados" / nome_arquivo
    with open(caminho, encoding="utf-8") as arquivo:
        return json.load(arquivo)