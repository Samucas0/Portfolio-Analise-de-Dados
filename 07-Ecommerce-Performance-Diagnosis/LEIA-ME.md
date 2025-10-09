[🇬🇧 For the English version, click here.](./README.md)

---

# Projeto 7: Diagnóstico de Performance de Produtos para E-commerce

## 🎯 Objetivo de Negócio
O objetivo deste projeto é analisar um grande dataset de transações de um e-commerce para identificar os 5 produtos com maior e menor faturamento. Esta análise visa gerar recomendações acionáveis para as equipes de gestão de estoque e marketing.

## 📚 Bibliotecas e Conceitos Utilizados
-   **Biblioteca:** `Pandas`
-   **Conceitos Principais:**
    -   Limpeza de Dados (uso de `.dropna()` e filtros com `.loc[]`)
    -   Engenharia de Features (criação da coluna `Faturamento`)
    -   Agregação de Dados com `.groupby()`
    -   Ranqueamento e Ordenação com `.sort_values()`
    -   Manipulação de grandes datasets (>1M de linhas)

## 📖 Descrição do Processo
1.  **Limpeza de Dados:** O dataset original continha entradas inválidas, como transações com quantidade negativa (devoluções), preços zerados e linhas sem descrição de produto. Um fluxo de limpeza foi executado para filtrar essas inconsistências e garantir a qualidade da análise.
2.  **Engenharia de Feature:** Uma nova coluna, `Faturamento`, foi criada multiplicando-se a `Quantidade` pelo `Preço` de cada transação.
3.  **Agregação:** O DataFrame limpo foi agrupado por produto (`Description`), e o faturamento total de cada produto foi calculado com `.sum()`.
4.  **Ranqueamento:** O resultado agregado final foi ordenado para identificar os 5 produtos no topo e na base do ranking de faturamento.

## 📊 Resultados e Insights
A análise identificou com sucesso os produtos campeões de venda, que são os principais motores de receita, bem como os produtos de baixa performance, que podem estar consumindo espaço valioso de estoque.

![alt text](image.png)

**Recomendação:**
-   **Top 5:** Garantir que estes produtos estejam sempre em estoque e considerá-los para campanhas de marketing em destaque.
-   **Bottom 5:** Avaliar se estes produtos devem ser descontinuados ou incluídos em uma liquidação para otimizar o estoque.

## 🗒️ Nota sobre o Idioma da Documentação
A partir deste projeto (Dia 7), adotei o **inglês como idioma padrão** para toda a documentação do meu portfólio (READMEs, comentários de código e mensagens de commit).

Esta mudança visa o alinhamento com os padrões da indústria de tecnologia global e a demonstração da minha proficiência no idioma para oportunidades internacionais. Para garantir a acessibilidade a todos os recrutadores no Brasil, a versão em português de cada documento (`LEIA-ME.md`) continuará disponível.

## 💡 Conclusão e Próximos Passos
Este projeto demonstra um fluxo de trabalho analítico completo e de ponta a ponta: desde a manipulação de um dataset grande e desorganizado do mundo real até a produção de uma recomendação de negócio clara e baseada em dados.

Como próximos passos, esta análise poderia ser expandida para:
1.  Visualizar os resultados com um gráfico de barras para facilitar a comunicação do insight.
2.  Investigar os produtos "problemáticos" para entender a causa do baixo faturamento.
3.  Analisar a performance dos produtos ao longo do tempo para identificar sazonalidade.