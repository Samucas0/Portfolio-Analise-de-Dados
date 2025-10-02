def calcular_valor_estoque(produto):
    """
    Calcula o valor total do estoque de um único produto.

    Args:
        produto (dict): Um dicionário representando um produto,
                      que deve conter as chaves 'preco' e 'qtd'.

    Returns:
        float: O valor total do estoque (preco * qtd),
               ou 0 se alguma das chaves estiver faltando.
    """
    # Checa de forma mais direta e em uma única linha se ambas as chaves existem no dicionário.
    if 'preco' in produto and 'qtd' in produto:
        total = produto['preco'] * produto['qtd']
        return total
    
    # Se as chaves não existirem, é uma boa prática retornar um valor padrão, como 0.
    return 0

# Dicionário representando um item do nosso estoque
produto_info = {
    'nome': 'Celular',
    'preco': 5000,
    'qtd': 15
}

# Chama a função e armazena o resultado
valor_total = calcular_valor_estoque(produto_info)

# Apresenta o resultado de forma clara
print(f'O valor total do estoque de {produto_info["nome"]} é: R${valor_total:.2f}')