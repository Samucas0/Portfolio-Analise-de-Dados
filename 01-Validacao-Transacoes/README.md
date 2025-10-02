# Projeto 1: Validador e Processador de Lote de Transações Financeiras

## 🎯 Objetivo de Negócio
O objetivo deste projeto foi desenvolver um script em Python para realizar a primeira etapa de qualquer análise financeira: a **validação e limpeza de dados brutos**. A ferramenta automatiza o processamento de um lote diário de transações, separando entradas válidas de inválidas e calculando métricas essenciais para um relatório gerencial rápido, garantindo a confiabilidade das análises subsequentes.

## 📚 Bibliotecas e Conceitos Utilizados
Este projeto foi desenvolvido utilizando apenas os conceitos fundamentais do Python 3, consolidando o aprendizado do primeiro dia de estudos:
-   Manipulação de Variáveis (Inteiros, `None`)
-   Estruturas de Dados (Listas)
-   Controle de Fluxo (Laços `for`)
-   Lógica Condicional (`if`/`else`)
-   Operadores Matemáticos e de Comparação

## 📖 Descrição do Processo
A análise foi estruturada em duas etapas, refletindo um processo de aprendizado e aplicação:

1.  **Exercício Prático de Fundamentação (`exercicio_pratico/filtro_pares.py`):**
    Antes de abordar o problema de negócio, foi desenvolvido um script menor para consolidar os conceitos do dia. O exercício consistiu em criar um programa que processa uma entrada de texto do usuário e filtra apenas os números pares. Este passo foi crucial para praticar a lógica de iteração com laços `for` e a tomada de decisão com condicionais `if`.

2.  **Desenvolvimento do Projeto Principal (`analise_transacoes.py`):**
    Com os conceitos fundamentais já praticados, a lógica foi aplicada ao problema de negócio. O script percorre uma lista de transações, valida cada uma, as segmenta em listas de "válidas" e "inválidas", e realiza os cálculos de soma, maior e menor valor em uma única passagem.

## 📊 Resultados e Insights
A execução do script no lote de dados fornecido (`[30000, 45000, ..., 23000]`) gerou o seguinte relatório:

-   **Volume Válido Total:** R$ 132.000,00
-   **Maior Transação do Lote:** R$ 45.000,00
-   **Menor Transação Válida:** R$ 12.000,00
-   **Média das Transações Válidas:** R$ 26.400,00
-   **Transações Inválidas Identificadas:** 3 (`[-29000, -20939, 0]`)

O principal insight desta análise é a identificação de 3 transações que não deveriam estar em um lote de vendas, representando um **risco à integridade dos dados**. Estas entradas precisam ser investigadas antes que análises mais profundas sejam realizadas.

## 💡 Conclusão e Próximos Passos
Este projeto, embora fundamental, demonstra a criação de uma ferramenta essencial para a **garantia da qualidade dos dados (Data Quality Assurance)**. A estrutura de aprendizado, partindo de um exercício prático para um problema de negócio, solidifica a capacidade de aplicar conceitos de programação para resolver problemas reais.

Como próximos passos para evoluir este projeto, poderíamos:
1.  Adaptar o script para ler os dados de um arquivo `.csv`.
2.  Salvar os relatórios de transações válidas e inválidas em arquivos de texto separados.
3.  **(Conceito do Dia 2)** Transformar a lógica em uma função para ser facilmente reutilizada.
