# Projeto 5: Relatório Gerencial de Vendas por Categoria de Produto

## 🎯 Objetivo de Negócio
O objetivo deste projeto é transformar uma lista de transações de vendas brutas em um relatório gerencial sumarizado. A análise visa agrupar os dados por categoria de produto para calcular KPIs (Key Performance Indicators) essenciais, como receita total, número de vendas e ticket médio, fornecendo uma visão clara da performance de cada categoria para a tomada de decisão.

## 📚 Bibliotecas e Conceitos Utilizados
Este projeto aprofunda o conhecimento na biblioteca Pandas, focando na sua funcionalidade mais poderosa para sumarização de dados.
-   **Bibliotecas:** `Pandas`
-   **Conceitos Principais:**
    -   **`.groupby()`:** A ferramenta central para dividir os dados em grupos com base em uma categoria.
    -   **Funções de Agregação:** `.sum()`, `.mean()`, `.count()` para calcular as métricas de cada grupo.
    -   **`.agg()`:** O método avançado para aplicar múltiplas agregações em uma única operação, otimizando o código.
    -   **Renomeação de Colunas:** `.rename()` para formatar o DataFrame final em um relatório profissional.

## 📖 Descrição do Processo
A criação do relatório seguiu uma abordagem estruturada:

1.  **Exercício Prático (`exercicio_pratico/custo_medio_categoria.py`):**
    Para aquecer, o conceito de agregação foi praticado de forma isolada, utilizando `groupby()` combinado com `.mean()` para calcular o custo médio por categoria.

2.  **Desenvolvimento do Projeto Principal (`relatorio_gerencial_vendas.ipynb`):**
    -   **Agrupamento:** O DataFrame de vendas foi agrupado pela coluna `Categoria`.
    -   **Agregação Múltipla:** O método `.agg()` foi utilizado para calcular a soma (`sum`), a contagem (`count`) e a média (`mean`) da coluna `Valor` para cada grupo, tudo em uma única linha de código.
    -   **Formatação do Relatório:** As colunas do DataFrame resultante foram renomeadas para nomes mais descritivos e claros (ex: `sum` para `Receita Total (R$)`), transformando a saída técnica em um relatório de negócio legível.

## 📊 Resultados e Insights
A análise resultou no seguinte relatório gerencial, que sumariza a performance de cada categoria de produto:

| Categoria | Receita Total (R$) | Nº de Vendas | Ticket Médio (R$) |
| :--- | :--- | :--- | :--- |
| Eletronicos | 3549.90 | 3 | 1183.30 |
| Livros | 95.50 | 2 | 47.75 |
| Vestuario | 325.00 | 2 | 162.50 |

**Insights Imediatos:**
-   A categoria **Eletrônicos** é, de longe, a que gera maior receita total.
-   Apesar de terem o mesmo número de vendas, **Vestuário** possui um ticket médio significativamente maior que **Livros**.

## 💡 Conclusão e Próximos Passos
Este projeto demonstra a capacidade de transformar dados transacionais brutos em um relatório agregado que gera insights de negócio. O uso de `.groupby().agg()` provou ser uma ferramenta extremamente eficiente e poderosa para a criação de sumários gerenciais.

Como próximos passos para esta análise:
1.  **(Assunto do Dia 6)** Enriquecer estes dados juntando-os (`.merge()`) com uma tabela de informações dos clientes para ver qual perfil de cliente compra cada categoria.
2.  **(Assunto do Dia 8)** Criar visualizações (gráficos de barras) para comparar a performance de cada categoria de forma mais intuitiva.
3.  Analisar a performance das categorias ao longo do tempo (usando a coluna `Data`).