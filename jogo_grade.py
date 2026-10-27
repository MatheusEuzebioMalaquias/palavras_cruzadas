from src.carregador import carregar_grade
from src.jogo import jogar_grade

dados_grade = carregar_grade("grade_teste.json")
pontos = jogar_grade(dados_grade)

print("\nFim de jogo! Pontuação:", pontos)