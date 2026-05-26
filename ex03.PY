# Exercício 3 — Função com responsabilidade única

def calcular_desconto(valor):
    if valor > 100:
        return valor * 0.1
    return 0

def calcular_valor_final(valor):
    desconto = calcular_desconto(valor)
    return valor - desconto

def exibir_dados(nome_cliente, valor):
    valor_final = calcular_valor_final(valor)
    print(f"Cliente: {nome_cliente}")
    print(f"Valor: R$ {valor:.2f}")
    print(f"Valor final com desconto: R$ {valor_final:.2f}")

# Exemplo de uso das funções:

exibir_dados("Ana Soares", 500)
 