[🇺🇸 For the English version, click here.](./README.md)

---

# Projeto 13: Painel Executivo de Vendas com Tabelas Dinâmicas

## 🎯 Objetivo de Negócio
O objetivo deste projeto é transformar dados transacionais brutos e granulares em um painel executivo de alto nível. Usando técnicas avançadas de remodelagem de dados, visamos responder a perguntas críticas de negócios, como "Quem é o representante de vendas com melhor desempenho?" e "Qual funcionário é especialista em qual categoria de produto?". Isso cria uma ferramenta para a gerência tomar decisões rápidas sobre bônus de desempenho e alocação de recursos sem precisar analisar milhares de linhas.

## 📚 Bibliotecas e Conceitos Usados
-   **Bibliotecas:** `Pandas`, `Seaborn`, `Numpy`
-   **Conceitos Chave:**
    -   **Remodelagem de Dados (`.pivot_table()`):** Transformar logs de transações em formato longo para matrizes em formato largo (wide) para comparação lado a lado.
    -   **Análise de Frequência (`.crosstab()`):** Contar ocorrências entre variáveis categóricas para entender distribuições e taxas.
    -   **Estilização de Dados (`.style`):** Usar o Pandas Styler para aplicar mapas de calor (heatmaps), barras de dados e formatação de moeda, transformando um DataFrame em um relatório pronto para apresentação.
    -   **Simulação de Dados:** Gerar dados de vendas fictícios realistas com `Numpy` para simular cenários de negócios.

## 📖 Descrição do Processo
1.  **Exercício Fundamental (`practice_exercise/titanic_crosstab_analysis.py`):**
    O dia começou com um script focado na diferença entre contagens brutas e taxas normalizadas. Usamos `pd.crosstab()` no dataset do Titanic para provar que, embora a 3ª classe tivesse mais passageiros, a 1ª classe teve uma *taxa de sobrevivência* (porcentagem) significativamente maior.

2.  **Projeto Principal (`sales_rep_performance_panel.ipynb`):**
    -   **Geração de Dados:** Um dataset sintético de 1.500 transações de vendas foi criado, simulando uma distribuição de Pareto onde existem poucos grandes negócios entre muitos menores.
    -   **Criação da Matriz:** Usamos `pivot_table` para agregar os valores de vendas, definindo `Sales_Rep` (Vendedor) como linhas e `Category` (Categoria) como colunas. Isso revelou instantaneamente os pontos fortes e fracos de cada membro da equipe.
    -   **Estilização do Painel:** Aplicamos um gradiente de calor (Verdes) para destacar especialistas em categorias e adicionamos barras de dados à coluna "Receita Total" para sinalizar visualmente os melhores desempenhos.

## 📊 Resultados e Insights
-   **Transformação:** Convertemos com sucesso um dataset de 1.500 linhas em uma matriz concisa de 6x5.
-   **Insight Estratégico:** O painel distingue claramente entre "Generalistas" (que vendem bem em todas as categorias) e "Especialistas" (que dominam um único nicho, como Hardware ou Consultoria).
-   **Valor de Negócio:** Este projeto demonstra como ir além da exportação básica de dados e fornecer aos stakeholders uma ferramenta visual e interativa que não requer software de BI adicional.

## 💡 Conclusão
Este projeto destaca o poder do Pandas não apenas para cálculo, mas para *comunicação*. Ao dominar tabelas dinâmicas e estilização, um analista pode entregar inteligência acionável diretamente em um notebook Python, preenchendo a lacuna entre código bruto e estratégia de negócios.