# O comentário acima é uma boa prática para garantir a compatibilidade com acentos.

# --- Bloco de Dados de Entrada ---
# Simula um lote de transações financeiras recebido para análise.
lista_de_transacoes = [30000, 45000, 22000, -29000, 12000, -20939, 0, 23000]

# --- Bloco de Inicialização de Variáveis ---
# Preparamos as "caixas" onde vamos guardar os resultados da nossa análise.
soma_das_validas = 0
maior_transacao_geral = lista_de_transacoes[0]
menor_transacao_valida = None  # Essencial para a lógica de encontrar a menor válida corretamente.

transacoes_validas = []
transacoes_invalidas = []

# --- Bloco de Processamento Principal ---
# O coração da análise: um laço 'for' que inspeciona cada transação, uma por uma.
for transacao_atual in lista_de_transacoes:

    # A primeira decisão é validar a transação.
    if transacao_atual > 0:
        transacoes_validas.append(transacao_atual)
        soma_das_validas += transacao_atual
        
        # Comentário do "Porquê": Esta lógica é necessária para garantir que a
        # 'menor_transacao_valida' comece com o PRIMEIRO valor válido encontrado
        # e não com um valor arbitrário que poderia gerar bugs.
        if menor_transacao_valida is None or transacao_atual < menor_transacao_valida:
            menor_transacao_valida = transacao_atual
    else:
        transacoes_invalidas.append(transacao_atual)
    
    # Independentemente da validação, checamos pela maior transação do lote inteiro.
    # O nome da variável 'maior_transacao_geral' já explica seu propósito.
    if transacao_atual > maior_transacao_geral:
        maior_transacao_geral = transacao_atual

# --- Bloco de Cálculos Finais ---
# Após o laço, com os dados processados, calculamos a média.
# Verificamos se a lista de válidas não está vazia para evitar um erro de divisão por zero.
if transacoes_validas:
    media_das_validas = soma_das_validas / len(transacoes_validas)
else:
    media_das_validas = 0

# --- Bloco de Apresentação dos Resultados ---
# Imprime um relatório formatado e claro no console. A apresentação é tão importante quanto a análise.
print("\n--- Relatório de Análise de Transações ---")
print(f"Volume total transacionado (soma das válidas): R${soma_das_validas:.2f}")
print(f"Maior transação registrada no lote: R${maior_transacao_geral:.2f}")

# Antes de imprimir a menor válida, verificamos se alguma foi encontrada.
if menor_transacao_valida is not None:
    print(f"Menor transação VÁLIDA registrada: R${menor_transacao_valida:.2f}")
else:
    print("Menor transação VÁLIDA registrada: Nenhuma transação válida encontrada.")

print(f"Média das transações válidas: R${media_das_validas:.2f}")
print("-" * 43)
print(f"Lista de transações válidas: {transacoes_validas}")
print(f"Lista de transações inválidas/nulas: {transacoes_invalidas}")
print("--- Fim do Relatório ---\n")