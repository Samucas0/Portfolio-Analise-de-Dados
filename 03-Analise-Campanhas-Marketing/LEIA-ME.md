[🇬🇧 For the English version, click here.](./README.md)

---

# Projeto 3: Simulação e Análise de Performance de Campanhas de Marketing (Teste A/B)

## 🎯 Objetivo de Negócio
O objetivo deste projeto foi realizar uma análise comparativa de performance entre duas campanhas de marketing simuladas (Teste A/B). A análise visa determinar qual campanha gerou melhores resultados (maior volume de cliques) e qual foi mais consistente (menor variação), fornecendo uma recomendação clara e baseada em dados para futuros investimentos.

## 📚 Bibliotecas e Conceitos Utilizados
-   **Biblioteca:** `NumPy`
-   **Conceitos Principais:**
    -   Arrays NumPy (`ndarray`) para computação numérica eficiente.
    -   Funções de Agregação Estatística (`.sum()`, `.mean()`, `.std()`).
    -   Modularização com Funções para criar blocos de análise reutilizáveis.
    -   Lógica Condicional (`if/else`) para automatizar a conclusão final.

## 📖 Descrição do Processo
1.  **Exercício Prático (`exercicio_pratico/calculadora_faturamento_numpy.py`):** Para consolidar o conceito de **vetorização**, foi desenvolvido um script que calcula o faturamento a partir de arrays de preços e quantidades, demonstrando a eficiência do NumPy.
2.  **Projeto Principal (`analise_teste_ab.ipynb`):**
    -   **Simulação dos Dados:** Foram criados dois arrays NumPy para simular os cliques diários de cada campanha.
    -   **Análise Modular:** Uma função, `analisar_campanha()`, foi criada para receber um array e retornar um dicionário com as métricas chave (média, desvio padrão, total).
    -   **Processamento e Comparação:** A função foi chamada para cada campanha.
    -   **Conclusão Automatizada:** Utilizando lógica condicional, o script compara as métricas de performance e estabilidade para gerar uma recomendação final de forma automática.

## 📊 Resultados e Insights
A análise gerou um relatório comparativo que demonstrou a clara superioridade da **Campanha 2**, que não apenas produziu um volume total e uma média de cliques maiores (performance superior), mas também o fez com uma variação diária muito menor (maior estabilidade).

## 💡 Conclusão
Este projeto demonstra a aplicação de análises estatísticas básicas para tomar uma decisão de negócio informada. O uso do NumPy permitiu cálculos rápidos, enquanto a estrutura do código transformou um simples cálculo em um pequeno sistema de apoio à decisão.