[🇺🇸 For the English version, click here.](./README.md)

---

# Projeto 14: Tendências de Séries Temporais e Análise de Sentimento (NLP)

## 🎯 Objetivo de Negócio
Este projeto serve como uma consolidação de habilidades analíticas avançadas, abordando dois domínios de negócios distintos, mas críticos: **Análise de Séries Temporais** e **Processamento de Linguagem Natural (NLP)**.
1.  **Séries Temporais:** Para entender as tendências de vendas ao longo do tempo, separar o sinal do ruído e identificar padrões de sazonalidade semanal para otimizar pessoal ou marketing.
2.  **NLP:** Para analisar o feedback não estruturado do cliente (avaliações), automatizar a pontuação de sentimento e identificar as causas raízes da rotatividade ou satisfação do cliente.

## 📚 Bibliotecas e Conceitos Usados
-   **Bibliotecas:** `Pandas`, `Numpy`, `Matplotlib`, `Seaborn`, `TextBlob`, `WordCloud`
-   **Conceitos Chave:**
    -   **Séries Temporais:** Reamostragem (`.resample()`), Médias Móveis (`.rolling()`) e propriedades de Datetime (acessor `.dt`).
    -   **NLP:** Pontuação de Polaridade de Sentimento, Pré-processamento de Texto, Nuvens de Palavras para visualização de texto não estruturado.
    -   **Correlação:** Analisar a relação entre o tamanho da avaliação e a satisfação do cliente.

## 📖 Descrição do Processo
1.  **Exercício Fundamental (`practice_exercise/stock_moving_avg.py`):**
    Começamos analisando as tendências do mercado de ações usando Funções de Janela. Geramos dados aleatórios e aplicamos uma Média Móvel de 7 e 30 dias para suavizar a volatilidade e visualizar a tendência subjacente de preço.

2.  **Projeto Principal - Parte 1: Séries Temporais (`sales_trend_analysis.ipynb`):**
    -   **Simulação:** Geramos dados de vendas por hora para um ano inteiro, injetando um padrão onde os fins de semana têm receita maior.
    -   **Análise:** Agregamos os dados para níveis diários/semanais e usamos uma Média Móvel de 30 dias para visualizar o crescimento. Também analisamos a sazonalidade por Dia da Semana para confirmar a hipótese do "Pico de Fim de Semana".

3.  **Projeto Principal - Parte 2: Análise de Sentimento (`product_review_analysis.ipynb`):**
    -   **Geração de Dados:** Criamos um dataset sintético de 500 avaliações de produtos usando templates de texto para imitar feedback positivo, negativo e neutro.
    -   **Engenharia de Atributos:** Calculamos `Sentiment_Score` (usando TextBlob) e `Review_Length` (tamanho do review).
    -   **Visualização:** Criamos um ranking dos melhores produtos com base no sentimento e uma Nuvem de Palavras destacando termos comuns em avaliações negativas (ex: "Bateria", "Quebrado").

## 📊 Resultados e Insights
-   **Séries Temporais:** Identificamos com sucesso que sábados e domingos geram ~$100/hora a mais de receita do que dias úteis, validando a necessidade de aumentar recursos no fim de semana.
-   **NLP:** Descobrimos uma correlação entre o sentimento da avaliação e a nota. A Nuvem de Palavras forneceu pistas visuais imediatas sobre defeitos do produto, mostrando que problemas de "Bateria" são o principal impulsionador de avaliações negativas.
-   **Versatilidade:** Demonstramos a capacidade de lidar tanto com dados temporais estruturados quanto com dados de texto não estruturados dentro do mesmo framework analítico.

## 💡 Conclusão
Este projeto preenche a lacuna entre a análise quantitativa e qualitativa. Ao dominar Séries Temporais, respondemos "Quando as vendas estão acontecendo?". Ao dominar NLP, respondemos "Por que os clientes estão comprando (ou saindo)?". Juntos, eles formam um kit de ferramentas completo para a Engenharia e Análise de Dados moderna.