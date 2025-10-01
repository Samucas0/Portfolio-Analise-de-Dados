# Importa a biblioteca 're' para trabalhar com Expressões Regulares.
# Embora o import seja um conceito um pouco mais avançado, o uso dele para
# dividir a entrada do usuário é uma solução prática que você descobriu.
import re

# Pede ao usuário para digitar uma string de números.
numeros_input = input('Digite uma lista de números (separados por vírgula ou espaço): ')

# Limpa a entrada do usuário e a divide em uma lista de strings.
# O padrão r'[, ]+' é uma forma robusta de lidar com diferentes separadores.
partes_texto = re.split(r'[, ]+', numeros_input.strip())

# --- Processamento ---
# Inicializa uma lista vazia para guardar os resultados.
pares_encontrados = []  

# Percorre cada 'pedaço' de texto na lista que foi gerada.
for texto_do_numero in partes_texto:
    
    # Converte o texto para um número inteiro para poder fazer o cálculo.
    numero = int(texto_do_numero)
    
    # O código em si já explica o QUE ele faz (checa se o resto da divisão por 2 é 0).
    # Não precisamos de mais comentários aqui, pois o código é claro.
    if numero % 2 == 0:
        pares_encontrados.append(numero)

# --- Saída ---
# Apresenta o resultado final ao usuário.
print(f'Os números pares encontrados foram: {pares_encontrados}')