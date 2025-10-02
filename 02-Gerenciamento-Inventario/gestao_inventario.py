import re

def adicionar_item(estoque):
    """Adiciona um produto e sua quantidade ao dicionário de estoque."""
    
    # Pede a entrada do usuário
    entrada = input('Digite o produto e a quantidade (ex: "maçã, 15"): ')
    partes = re.split(r'[, ]+', entrada.strip())

    # Validação da entrada
    if len(partes) != 2:
        print("Erro: Entrada inválida. Por favor, forneça um produto e uma quantidade.")
        return # Retorna para o menu principal

    produto = partes[0].lower() # Padroniza o nome do produto para minúsculas
    
    # Bloco try-except para tratar erros de conversão de forma segura
    try:
        quantidade = int(partes[1])
        estoque[produto] = quantidade
        print(f'Sucesso: {produto} com {quantidade} unidades foi adicionado ao estoque.')
    except ValueError:
        # Este bloco é executado se int() falhar (ex: usuário digitou 'quinze')
        print(f"Erro: A quantidade '{partes[1]}' não é um número válido.")

def remover_item(estoque):
    """Remove um produto do dicionário de estoque."""
    
    produto_a_remover = input('Digite o produto a ser removido: ').strip().lower()

    # Checa se o item realmente existe no estoque antes de tentar remover
    if produto_a_remover in estoque:
        del estoque[produto_a_remover]
        print(f'Sucesso: {produto_a_remover} foi removido do estoque.')
    else:
        print(f'Erro: O produto "{produto_a_remover}" não foi encontrado no estoque.')

def gerar_relatorio_estoque(estoque):
    """Exibe todos os produtos e suas quantidades no estoque."""
    
    print("\n--- Relatório de Estoque Atual ---")
    if not estoque: # Checa se o dicionário está vazio
        print("O estoque está vazio.")
    else:
        # Itera pelo dicionário e imprime cada item de forma formatada
        for produto, quantidade in estoque.items():
            print(f'- {produto.capitalize()}: {quantidade} unidades')
    print("---------------------------------\n")

# --- Bloco Principal de Execução ---
# Esta é a parte que controla a aplicação e o menu interativo.
if __name__ == "__main__":
    
    # Inicializa o estoque com alguns itens de exemplo
    estoque_loja = {
        'banana': 38,
        'laranja': 22,
        'uva': 50
    }
    
    # Laço infinito que mantém o menu rodando até o usuário decidir sair
    while True:
        print("\n--- Menu de Gerenciamento de Estoque ---")
        print("1: Adicionar Item")
        print("2: Remover Item")
        print("3: Ver Relatório de Estoque")
        print("4: Sair")
        
        escolha = input("Digite o número da sua escolha: ")

        if escolha == '1':
            adicionar_item(estoque_loja)
        elif escolha == '2':
            remover_item(estoque_loja)
        elif escolha == '3':
            gerar_relatorio_estoque(estoque_loja)
        elif escolha == '4':
            print("Saindo do programa. Até logo!")
            break # Quebra o laço infinito e encerra o programa
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 4.")