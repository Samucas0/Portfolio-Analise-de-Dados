[🇬🇧 For the English version, click here.](./README.md)

---

# Projeto 8: Relatório Visual de Variação de Custo de Matéria-Prima

## 🎯 Objetivo de Negócio
O objetivo deste projeto foi criar um relatório visual claro e informativo para acompanhar a flutuação de preço de matérias-primas essenciais ao longo do tempo. Em vez de apenas apresentar uma tabela de números, a meta era usar a visualização de dados para destacar tendências, picos e vales de forma imediata, permitindo uma tomada de decisão mais rápida e intuitiva para as equipes de finanças e supply chain.

## 📚 Bibliotecas e Conceitos Utilizados
Este projeto introduz a biblioteca fundamental para a visualização de dados em Python.
-   **Biblioteca:** `Matplotlib`
-   **Conceitos Principais:**
    -   **Gráficos de Linha (`plt.plot`):** Utilizados para mostrar a evolução de uma variável no tempo.
    -   **Gráficos de Barra (`plt.bar`):** Utilizados para comparar quantidades entre categorias.
    -   **Customização de Gráficos:** Adição de títulos, rótulos (`xlabel`, `ylabel`) e legendas (`legend`).
    -   **Anotações (`plt.annotate`):** A habilidade chave deste projeto, usada para destacar e adicionar comentários a pontos de dados específicos, guiando a atenção do leitor.

## 📖 Descrição do Processo
1.  **Exercício Prático (`practice_exercise/sales_goals_chart.py`):**
    O dia começou com um exercício prático para comparar dados categóricos. Foi criado um gráfico de barras para mostrar a performance de diferentes vendedores e uma linha horizontal (`plt.axhline`) foi adicionada para representar uma meta de vendas, praticando a combinação de diferentes tipos de plots.

2.  **Projeto Principal (`raw_material_cost_report.ipynb`):**
    -   **Simulação dos Dados:** Foram criados dados fictícios de custo mensal para três matérias-primas (Aço, Cobre, Alumínio).
    -   **Plotagem Dinâmica:** Um laço `for` foi implementado para plotar a evolução de custo de cada material, tornando o código escalável e limpo.
    -   **Destaque de Insights:** A função `plt.annotate()` foi utilizada para encontrar e rotular automaticamente o pico de custo do 'Cobre' e o ponto de custo mais baixo do 'Aço'. Isso transforma o gráfico de uma simples visualização para uma ferramenta analítica que aponta ativamente os eventos importantes.

## 📊 Resultado
O resultado final é um gráfico de linha que não apenas exibe as tendências de custo para todos os materiais, mas também usa setas e anotações de texto para chamar a atenção explicitamente para as variações de preço mais significativas, fornecendo insights imediatos sem exigir análise manual do espectador.

## 💡 Conclusão
Este projeto demonstra o princípio fundamental do "storytelling com dados": uma boa visualização não é apenas sobre mostrar os dados, mas sobre **comunicar o insight** escondido neles. O uso de anotações provou ser uma técnica poderosa para guiar a narrativa e tornar as conclusões do relatório instantaneamente compreensíveis.