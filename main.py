from src.carregador import carregar_dados, carregar_grade
from src.jogo import jogar_grade
from src.menu import escolher
from src.progresso import carregar_progresso, salvar_progresso


def main():
    dados = carregar_dados()
    progresso = carregar_progresso()

    print("=" * 40)
    print("PALAVRAS CRUZADAS DE ESTUDO")
    print("=" * 40)

    topicos = dados["topicos"]
    posicao = escolher("Tópico de estudo:", [t["nome"] for t in topicos])
    if posicao is None:
        return
    topico = topicos[posicao]

    assuntos = topico["assuntos"]
    posicao = escolher("Assunto:", [a["nome"] for a in assuntos])
    if posicao is None:
        return
    assunto = assuntos[posicao]

    fases = assunto["fases"]
    if not fases:
        print("\nEste assunto ainda não tem fases. Em breve!")
        return

    chave = f"{topico['nome']} / {assunto['nome']}"
    fase_atual = progresso.get(chave, 1)

    fase = None
    for f in fases:
        if f["numero"] == fase_atual:
            fase = f

    if fase is None:
        print("\nVocê concluiu todas as fases disponíveis deste assunto!")
        return

    minimo = fase["pontos_minimos"]
    print(f"\nFase {fase['numero']}: mínimo de {minimo} pontos para avançar")

    dados_grade = carregar_grade(fase["grade"])
    pontos = jogar_grade(dados_grade)

    print(f"\nFim da fase! Pontuação: {pontos}")

    if pontos >= minimo:
        progresso[chave] = fase_atual + 1
        salvar_progresso(progresso)
        print("Parabéns, você passou de fase!")
    else:
        print(f"Faltaram {minimo - pontos} pontos. Tente de novo!")


if __name__ == "__main__":
    main()