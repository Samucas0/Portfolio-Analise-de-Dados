[🇬🇧 For the English version, click here.](./README.md)

---

# Projeto 1: Validador e Processador de Lote de Transações Financeiras

## 🎯 Objetivo de Negócio
O objetivo deste projeto foi desenvolver um script em Python para realizar a primeira etapa de qualquer análise financeira: a **validação e limpeza de dados brutos**. A ferramenta automatiza o processamento de um lote diário de transações, separando entradas válidas de inválidas e calculando métricas essenciais para um relatório gerencial rápido, garantindo a confiabilidade das análises subsequentes.

## 📚 Bibliotecas e Conceitos Utilizados
-   Fundamentos de Python 3
-   Estruturas de Dados: Listas
-   Controle de Fluxo: Laços `for`
-   Lógica Condicional: `if/else`
-   Manipulação de Variáveis e Operadores Matemáticos

## 📖 Descrição do Processo
1.  **Exercício Prático (`exercicio_pratico/filtro_pares.py`):** Antes de abordar o problema de negócio, foi desenvolvido um script menor para praticar a iteração em listas e a lógica condicional, filtrando números pares de uma entrada do usuário.
2.  **Projeto Principal (`analise_transacoes.py`):** A lógica central foi aplicada ao problema de negócio. O script percorre uma lista de transações, valida cada uma (valor > 0), as segmenta em listas de "válidas" e "inválidas", e calcula a soma, o maior e o menor valor válido em uma única passagem.

## 📊 Resultados e Insights
O script processou com sucesso o lote de dados, identificando métricas chave e problemas de qualidade. O principal insight foi a identificação de transações inválidas (negativas ou nulas), que representam um risco à integridade dos dados e precisam ser investigadas.

## 💡 Conclusão
Este projeto fundamental demonstra a capacidade de automatizar tarefas de garantia de qualidade dos dados (Data Quality Assurance), um processo manual e sujeito a erros. Ele estabelece a base para a construção de fluxos de trabalho analíticos mais complexos.