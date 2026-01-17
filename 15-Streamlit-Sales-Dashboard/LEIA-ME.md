[🇺🇸 For the English version, click here.](./README.md)

---

# Projeto 15: Dashboard de Vendas Interativo com Streamlit

## 🎯 Objetivo de Negócio
O objetivo deste projeto é ir além dos relatórios estáticos (como PDFs ou planilhas Excel) e construir uma **Ferramenta de BI Self-Service**. Ao criar uma aplicação web interativa, empoderamos os stakeholders (gerentes, diretores) para explorar dados de vendas, aplicar filtros dinamicamente e responder às suas próprias perguntas sem precisar solicitar uma nova consulta SQL ao time de dados.

## 💡 A Curva de Aprendizado
Este projeto representou um marco importante na minha jornada. Diferente de scripts de análise comuns, construir uma aplicação web exigiu um mergulho profundo em conceitos de **Engenharia de Software** e **Gestão de Ambientes**.
Dediquei um tempo considerável para dominar a infraestrutura de "bastidores": configuração de ambientes virtuais (`.venv`), gerenciamento de dependências com `pip` e a execução de servidores locais via terminal. Essa experiência foi fundamental para preencher a lacuna entre a Análise de Dados e a Engenharia de Dados.

## 📚 Bibliotecas e Conceitos Usados
-   **Streamlit:** Para converter scripts Python em uma aplicação web implantável instantaneamente.
-   **Plotly Express:** Para criar gráficos interativos (zoom, hover, tooltips).
-   **Pandas:** Para manipulação de dados e lógica de filtragem (query).
-   **Numpy:** Para gerar dados de vendas sintéticos e realistas.

## 🚀 Como Rodar
1.  Certifique-se de ter as dependências instaladas:
    ```bash
    pip install streamlit plotly pandas
    ```
2.  Execute o aplicativo pelo terminal:
    ```bash
    streamlit run 15-Streamlit-Sales-Dashboard/app.py
    ```
3.  O dashboard abrirá automaticamente no seu navegador (geralmente em `http://localhost:8501`).

## 📊 Principais Funcionalidades
-   **Filtragem Dinâmica:** Controles na barra lateral permitem que os usuários segmentem os dados por Região e Produto.
-   **Métricas de KPI:** Cálculo em tempo real da Receita Total, Ticket Médio e Unidades Vendidas com base nos filtros ativos.
-   **Visualizações Interativas:**
    -   *Gráfico de Barras:* Classificação de produtos por desempenho de receita.
    -   *Gráfico de Linha:* Análise de tendências mensais de vendas para identificar sazonalidade.