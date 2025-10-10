[🇬🇧 For the English version, click here.](./README.md)

---

# Projeto 2: Mini-Sistema de Gerenciamento de Inventário de Produtos

## 🎯 Objetivo de Negócio
O objetivo deste projeto foi desenvolver uma aplicação de console interativa para automatizar o controle básico de um inventário. A ferramenta visa substituir processos manuais, centralizando a adição, remoção e visualização de produtos em estoque, garantindo maior controle e reduzindo a chance de erros.

## 📚 Bibliotecas e Conceitos Utilizados
-   **Bibliotecas:** `re` (para tratamento de input)
-   **Conceitos Principais:**
    -   **Funções:** Modularização do código em blocos reutilizáveis e com responsabilidades únicas.
    -   **Dicionários:** Utilizados como a estrutura de dados principal para armazenar o inventário.
    -   **Lógica Condicional:** `if/elif/else` para controlar o fluxo do menu interativo.
    -   **Laços:** `while` para manter a aplicação em execução e `for` para iterar sobre o inventário.
    -   **Tratamento de Exceções:** `try-except` para garantir a robustez da aplicação.

## 📖 Descrição do Processo
1.  **Exercício Prático (`exercicio_pratico/calculadora_estoque.py`):** Primeiramente, um script simples foi desenvolvido para praticar a criação de uma função que opera sobre um dicionário, consolidando o conceito do dia.
2.  **Modularização:** A aplicação principal foi dividida em três funções centrais: `adicionar_item()`, `remover_item()` e `gerar_relatorio_estoque()`.
3.  **Interface Interativa:** O bloco de execução principal (`if __name__ == "__main__":`) contém um laço `while True` que cria um menu de console, transformando o script em uma aplicação interativa.
4.  **Robustez:** Foram implementadas validações de entrada e um bloco `try-except` para garantir que o programa não quebre com entradas inválidas do usuário.

## 📊 Resultado
O resultado final é uma aplicação de console funcional que simula um sistema de gerenciamento de estoque real, capaz de lidar com interações do usuário, atualizar dados e gerar relatórios.

## 💡 Conclusão
Este projeto foi um passo fundamental para sair de scripts lineares e começar a construir aplicações estruturadas e reutilizáveis. A lição principal foi a importância de dividir um problema em partes menores e gerenciáveis através de funções.