[🇬🇧 For the English version, click here.](./README.md)

---

# Projeto 5: Relatório Gerencial de Vendas por Categoria de Produto

## 🎯 Objetivo de Negócio
O objetivo deste projeto é transformar uma lista de transações de vendas brutas em um relatório gerencial sumarizado. A análise visa agrupar os dados por categoria de produto para calcular KPIs essenciais, como receita total, número de vendas e ticket médio, fornecendo uma visão clara da performance de cada categoria.

## 📚 Bibliotecas e Conceitos Utilizados
-   **Biblioteca:** `Pandas`
-   **Conceitos Principais:**
    -   `.groupby()`: Ferramenta central para dividir os dados em grupos.
    -   Funções de Agregação: `.sum()`, `.mean()`, `.count()`.
    -   `.agg()`: Método para aplicar múltiplas agregações em uma única operação.
    -   Renomeação de Colunas: `.rename()` para formatar o DataFrame final.

## 📖 Descrição do Processo
1.  **Exercício Prático (`exercicio_pratico/custo_medio_categoria.py`):** Para aquecer, o conceito de agregação foi praticado de forma isolada, usando `groupby()` com `.mean()` para calcular o custo médio por categoria.
2.  **Projeto Principal (`relatorio_gerencial_vendas.ipynb`):**
    -   **Agrupamento:** O DataFrame de vendas foi agrupado pela coluna `Categoria`.
    -   **Agregação Múltipla:** O método `.agg()` foi utilizado para calcular a soma (`sum`), a contagem (`count`) e a média (`mean`) da coluna `Valor` para cada grupo de uma só vez.
    -   **Formatação do Relatório:** As colunas do DataFrame resultante foram renomeadas para nomes mais descritivos e claros (ex: `sum` para `Receita Total (R$)`).

## 📊 Resultados e Insights
A análise resultou em um relatório gerencial que sumariza a performance de cada categoria, destacando que 'Eletronicos' é a categoria de maior faturamento, enquanto 'Vestuário' possui um ticket médio superior ao de 'Livros'.

## 💡 Conclusão
Este projeto demonstra a capacidade de transformar dados transacionais brutos em um relatório agregado que gera insights de negócio. O uso de `.groupby().agg()` provou ser uma ferramenta eficiente e poderosa para a criação de sumários gerenciais.