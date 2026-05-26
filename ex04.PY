# Exercício 4 — Evitando números mágicos

valor_minimo_frete_gratis= 200
valor_padrao_frete = 25

def calcular_frete(valor_compra):
    if valor_compra >= valor_minimo_frete_gratis:
        return 0
    return valor_padrao_frete

#Exemplo de uso da função 

print(f"Valor do frete para compras de até R$199,99: R${calcular_frete(199.99):.2f}")
print(f"Valor do frete para compras a partir de R$200,00: R${calcular_frete(200):.2f}")