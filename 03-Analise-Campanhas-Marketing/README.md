# Projeto 3: Simulação e Análise de Performance de Campanhas de Marketing (Teste A/B)

## 🎯 Objetivo de Negócio
O objetivo deste projeto foi realizar uma análise comparativa de performance entre duas campanhas de marketing simuladas, utilizando a metodologia de Teste A/B. A análise visa determinar qual campanha gerou melhores resultados (maior volume de cliques) e qual foi mais consistente (menor variação), fornecendo uma recomendação clara e baseada em dados para a alocação de futuros investimentos de marketing.

## 📚 Bibliotecas e Conceitos Utilizados
Este projeto introduz a biblioteca fundamental para computação científica em Python e solidifica o uso de funções.
-   **Bibliotecas:** `NumPy`
-   **Conceitos Principais:**
    -   **Arrays NumPy (`ndarray`):** Utilizados para armazenar e manipular os dados numéricos de forma eficiente.
    -   **Funções de Agregação:** `.sum()`, `.mean()`, `.std()` para calcular o total, a média e o desvio padrão dos dados.
    -   **Modularização com Funções:** Encapsulamento da lógica de análise para evitar repetição de código e aumentar a clareza.
    -   **Lógica Condicional (`if/else`):** Para automatizar a tomada de decisão e a geração da conclusão final.

## 📖 Descrição do Processo

1.  **Exercício Prático (`exercicio_pratico/calculadora_faturamento_numpy.py`):**
    Para consolidar o conceito de **vetorização**, foi desenvolvido um script inicial que calcula o faturamento a partir de arrays de preços e quantidades. Este exercício demonstrou o poder do NumPy em realizar operações matemáticas em múltiplos elementos de uma só vez, sem a necessidade de laços `for`.

2.  **Desenvolvimento do Projeto Principal (`analise_teste_ab.ipynb`):**
    -   **Simulação dos Dados:** Foram criados dois arrays NumPy (`cliques_campanha1` e `cliques_campanha2`) para simular os cliques diários de cada campanha.
    -   **Análise Modular:** Uma função, `analisar_campanha()`, foi criada para receber um array de dados e retornar um dicionário com as métricas chave (média, desvio padrão, total). Isso garantiu que a mesma análise fosse aplicada de forma consistente às duas campanhas.
    -   **Processamento e Comparação:** A função foi chamada para cada campanha, e os resultados foram armazenados.
    -   **Conclusão Automatizada:** Utilizando condicionais `if/else`, o script compara as métricas de performance (média) and estabilidade (desvio padrão) de ambas as campanhas para gerar uma recomendação final de forma automática.

## 📊 Resultados e Insights
A análise gerou o seguinte relatório comparativo:

**[ Campanha 1 ]**
-   Média de cliques diários: 550.80
-   Desvio Padrão: 28.29
-   Total de Cliques: 2754

**[ Campanha 2 ]**
-   Média de cliques diários: 608.40
-   Desvio Padrão: 7.63
-   Total de Cliques: 3042

O principal insight é a clara superioridade da **Campanha 2**. Ela não apenas gerou um volume total e uma média de cliques **superiores** (maior performance), como também o fez com uma variação diária muito menor, indicada por um **desvio padrão significativamente mais baixo** (maior estabilidade e previsibilidade).

## 💡 Conclusão e Próximos Passos
Este projeto demonstra a aplicação de análises estatísticas básicas para tomar uma decisão de negócio informada. A utilização do NumPy permitiu um cálculo rápido e limpo, enquanto a estruturação do código com funções e lógica condicional transformou um simples cálculo em um pequeno sistema de apoio à decisão.

Como próximos passos, esta análise poderia ser expandida para:
1.  Utilizar testes de hipótese estatística (como o Teste-T) para confirmar se a diferença entre as campanhas é estatisticamente significativa.
2.  Analisar o custo de cada campanha para calcular o "Custo por Clique" (CPC) e avaliar o retorno sobre o investimento (ROI).
3.  **(Assunto futuro)** Carregar os dados de um arquivo `.csv` utilizando a biblioteca **Pandas**.