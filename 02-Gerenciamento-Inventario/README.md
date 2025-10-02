# Projeto 2: Mini-Sistema de Gerenciamento de Inventário de Produtos

## 🎯 Objetivo de Negócio
O objetivo deste projeto foi desenvolver uma aplicação de console interativa para automatizar o controle básico de um inventário de produtos. A ferramenta visa substituir processos manuais de anotação, centralizando a adição, remoção e visualização de itens em estoque, garantindo maior controle e reduzindo a chance de erros operacionais.

## 📚 Bibliotecas e Conceitos Utilizados
Este projeto aprofunda os fundamentos do Python, com foco especial na organização de código através de funções.
-   **Bibliotecas:** `re` (para tratamento de input do usuário).
-   **Conceitos Principais:**
    -   **Funções:** Modularização do código em blocos reutilizáveis e com responsabilidades únicas.
    -   **Dicionários:** Utilizados como a estrutura de dados principal para armazenar o inventário (produto: quantidade).
    -   **Lógica Condicional:** `if`/`elif`/`else` para controlar o fluxo do menu interativo.
    -   **Laços:** `while` para manter a aplicação em execução e `for` para iterar sobre o inventário.
    -   **Tratamento de Exceções:** `try-except` para garantir a robustez da aplicação ao lidar com entradas inválidas do usuário.

## 📖 Descrição do Processo
A construção do sistema seguiu uma abordagem modular e interativa:

1.  **Exercício Prático (`exercicio_pratico/calculadora_estoque.py`):** Primeiramente, foi desenvolvido um script simples para praticar a criação de uma função que opera sobre um dicionário, consolidando o conceito principal do dia.

2.  **Modularização:** A aplicação principal foi dividida em três funções centrais, cada uma com uma responsabilidade clara: `adicionar_item()`, `remover_item()` e `gerar_relatorio_estoque()`.

3.  **Estrutura de Dados:** Um dicionário Python foi utilizado para representar o estoque, aproveitando sua eficiência na busca e modificação de itens através de chaves (nomes dos produtos).

4.  **Interface Interativa:** O bloco de execução principal (`if __name__ == "__main__":`) contém um laço `while True` que cria um menu de console. Isso transforma o script em uma aplicação interativa, onde o usuário pode escolher qual ação deseja realizar.

5.  **Robustez:** Foram implementadas validações de entrada e um bloco `try-except` na função de adicionar item, garantindo que o programa não quebre caso o usuário digite uma quantidade não numérica.

## 📊 Resultado: Uma Aplicação de Console Funcional
O resultado final é uma aplicação de console que simula um sistema de gerenciamento de estoque real. Um exemplo de interação com o usuário seria:

```bash
--- Menu de Gerenciamento de Estoque ---
1: Adicionar Item
2: Remover Item
3: Ver Relatório de Estoque
4: Sair
Digite o número da sua escolha: 3

--- Relatório de Estoque Atual ---
- Banana: 38 unidades
- Laranja: 22 unidades
- Uva: 50 unidades
---------------------------------

--- Menu de Gerenciamento de Estoque ---
1: Adicionar Item
2: Remover Item
3: Ver Relatório de Estoque
4: Sair
Digite o número da sua escolha: 1
Digite o produto e a quantidade (ex: "maçã, 15"): maca, 25
Sucesso: maca com 25 unidades foi adicionado ao estoque.

--- Menu de Gerenciamento de Estoque ---
1: Adicionar Item
2: Remover Item
3: Ver Relatório de Estoque
4: Sair
Digite o número da sua escolha: 4
Saindo do programa. Até logo!
