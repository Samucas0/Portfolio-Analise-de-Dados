[🇬🇧 For the English version, click here.](./README.md)

---

# Projeto 12: Engenharia de Features RFM para Segmentação de Clientes

## 🎯 Objetivo de Negócio
O objetivo deste projeto é transformar um dataset bruto de log transacional (onde cada linha é um *item*) em um DataFrame estruturado e centrado no cliente (onde cada linha é um *cliente*). Ao criar as três features centrais do RFM (Recência, Frequência, Valor), podemos criar a base para uma segmentação avançada de clientes. Isso permite que uma empresa deixe de analisar vendas individuais para entender o comportamento do cliente, identificando clientes de alto valor, em risco e perdidos.

## 📚 Bibliotecas e Conceitos Utilizados
-   **Bibliotecas:** `Pandas`, `Numpy`
-   **Conceitos Chave:**
    -   **Engenharia de Features (Feature Engineering):** O tema central; criação de novas colunas informativas (`TotalValue`, `Recency`, `Frequency`, `Monetary`) a partir de dados brutos.
    -   **Features de Nível de Linha (`.apply()`):** Uso de uma função personalizada com `.apply()` para criar uma nova coluna categórica baseada na lógica de uma única linha.
    -   **Features de Nível de Agregação (`.groupby().agg()`):** Uso de uma operação `groupby` para "comprimir" informações de muitas linhas (todas as transações de um cliente) em features de resumo únicas (`sum`, `nunique`, lógica `lambda`).
    -   **Limpeza de Dados:** Lidar com problemas de encoding (`'latin1'`), filtrar dados irrelevantes (`.dropna()`) e remover entradas inválidas (quantidades negativas).
    -   **Manipulação de Datas:** Uso de `pd.to_datetime` e `pd.Timedelta` para calcular diferenças de datas para a Recência.

## 📖 Descrição do Processo
1.  **Exercício de Fixação (`practice_exercise/age_categorizer.py`):** O dia começou com um exercício focado em engenharia de features em nível de linha. Uma função personalizada foi definida para categorizar idades e, em seguida, aplicada usando o método `.apply()` para criar uma nova coluna `age_group`, praticando a criação de features categóricas.
2.  **Projeto Principal (`rfm_customer_segmentation.ipynb`):**
    -   **Preparação dos Dados:** O dataset 'Online Retail' foi carregado, lidando com um encoding não padrão (`'latin1'`). Os dados foram limpos removendo pedidos cancelados (`Quantity` negativa) e entradas com `CustomerID` nulo.
    -   **Engenharia de Features (Nível Linha):** Uma coluna `TotalValue` foi criada multiplicando `Quantity` e `UnitPrice`. A coluna `InvoiceDate` foi convertida para o formato datetime adequado.
    -   **Engenharia de Features (Agregação RFM):** Uma `snapshot_date` (representando o "hoje") foi definida. O DataFrame foi então agrupado por `CustomerID` e o método `.agg()` foi usado para calcular as três features RFM:
        -   **Recência (R):** Dias desde a última compra (calculado usando uma função `lambda`).
        -   **Frequência (F):** Contagem de entradas `InvoiceNo` únicas.
        -   **Valor (M):** Soma da coluna `TotalValue`.

## 📊 Resultados & Insights
-   **Transformação:** O resultado principal é um novo e poderoso DataFrame onde cada linha representa unicamente um *cliente* e seus scores R, F e M calculados. O dataset foi transformado com sucesso do **nível de transação** para o **nível de cliente**.
-   **Aprendizado Chave:** Este projeto destacou os dois tipos principais de engenharia de features: nível de linha (usando `.apply()`) e nível de agregação (usando `.groupby().agg()`). Ambos são essenciais, e a escolha depende do problema.
-   **Valor de Negócio:** O `rfm_df` final está agora pronto para a etapa de *análise*. Uma empresa pode agora filtrar facilmente por "Melhores Clientes" (Baixo R, Alta F, Alto M) ou "Clientes em Risco" (Alto R, Alta F).

## 💡 Conclusão
Este projeto demonstra a capacidade crítica de manipular e reestruturar dados brutos para construir features comportamentais significativas. Ao criar a tabela RFM, traduzimos com sucesso um simples log de transações em uma ferramenta estratégica para entender personas de clientes, permitindo marketing direcionado e tomada de decisões baseadas em dados para melhorar a retenção de clientes.