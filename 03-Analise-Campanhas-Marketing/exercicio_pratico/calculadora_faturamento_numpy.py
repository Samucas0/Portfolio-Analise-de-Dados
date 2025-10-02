# Importa a biblioteca NumPy, fundamental para computação numérica.
import numpy as np

# Cria dois arrays NumPy: um para os preços e outro para as quantidades.
# A ordem dos elementos é importante e deve corresponder (preço[0] é do produto qtd[0]).
precos = np.array([40.00, 55.00, 26.00, 19.00, 32.00])
qtd = np.array([20, 15, 35, 50, 10])

# --- Processamento ---
# Calcula o faturamento por produto usando a "vetorização".
# O NumPy multiplica cada elemento do array 'precos' pelo elemento correspondente em 'qtd' de uma só vez.
faturamento_por_produto = precos * qtd

# Calcula o faturamento total usando a função de agregação .sum()
# Ela soma todos os valores dentro do array 'faturamento_por_produto'.
faturamento_total = faturamento_por_produto.sum()

# --- Apresentação dos Resultados ---
print('\n----- FATURAMENTO POR PRODUTO -----')
print(faturamento_por_produto, '\n')

print('----- FATURAMENTO TOTAL -----')
# Formata a saída do faturamento total para exibir como moeda.
print(f'R$ {faturamento_total:.2f}')