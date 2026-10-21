# Palavras Cruzadas de Estudo

Jogo de palavras cruzadas para estudar, feito em Python e jogado no terminal.
O jogador recebe dicas, tem 3 tentativas por palavra e vê as letras aparecerem
nos cruzamentos da grade conforme acerta.

## Funcionalidades

- Dicas e respostas carregadas de arquivos JSON (conteúdo separado do código)
- 3 tentativas por palavra e pontuação
- Grade com palavras que se cruzam, montada a partir de coordenadas
- Validação de cruzamentos: avisa a casa exata onde duas palavras discordam
- Respostas aceitas com ou sem acento e em maiúsculas ou minúsculas

## Como rodar

Requisitos: Python 3.8 ou superior. Nenhuma biblioteca externa é necessária.

```
git clone https://github.com/MatheusEuzebioMalaquias/palavras_cruzadas.git
cd palavras_cruzadas
python jogo_grade.py
```

Para jogar o modo simples (uma palavra por vez): `python main.py`

## Estrutura do projeto

```
dados/    arquivos JSON com tópicos, fases, palavras e dicas
src/      código do jogo (carregador, regras, grade e visual)
main.py   modo simples: uma dica por vez
jogo_grade.py   modo grade com cruzamentos
```

## Próximos passos

- Menu de tópicos (Tecnologia, Português, Matemática, PRF para concursos)
- Avançar de fase com pontuação mínima e salvar o progresso
- Grades totalmente preenchidas
- Versão web com Flask

## O que estou aprendendo com este projeto

Lógica de programação, organização de código em módulos, leitura de JSON,
estruturas de dados (listas, dicionários e conjuntos) e versionamento com Git.