# Pipeline de Extração, Limpeza, Transformação e Enriquecimento de Dados

Este projeto realiza um pipeline de dados com as seguintes etapas:

## Jobs

### Job 1 - Inserção de Dados
Carrega todos os registros do arquivo CSV para um banco de dados SQLite.

### Job 2 - Filtragem
Carrega apenas registros com quantidade de produção superior a 10.

### Job 3 - Limpeza de Dados
Remove o ponto (.) da coluna `receita_total` para evitar truncamento de números.

### Job 4 - Enriquecimento de Dados
Adiciona a coluna `margem_lucro`, calculada como `(receita_total / quantidade) - preco_medio`.

### Job 5 - Classificação de Preço
Classifica os produtos como "Caro" ou "Barato" com base no preço médio (superior a 15 é "Caro").

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
1. Rode o Programa:
   ```bash
   python pipeline.py
 Lembrando que para rodar o programa precisa ter instalado o DB Browser for SQLITE, para poder criar o banco lá e colocar os dados também.
