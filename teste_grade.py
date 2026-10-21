from src.carregador import carregar_grade
from src.grade import montar_quadro
from src.visual import desenhar_quadro

dados_grade = carregar_grade("grade_teste.json")
quadro = montar_quadro(dados_grade)
desenhar_quadro(quadro)