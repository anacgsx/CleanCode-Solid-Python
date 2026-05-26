# Exercício 2 — Removendo código duplicado

def calcular_desconto(preco, taxa_desconto):
    desconto = preco * taxa_desconto
    preco_final= preco - desconto
    return preco_final

# Exemplo de uso da função:

preco_final_1 = calcular_desconto(100, 0.10)
preco_final_2 = calcular_desconto(250, 0.10)
preco_final_3 = calcular_desconto(80, 0.10)
print(f"Produto 1: R$ {preco_final_1:.2f}")
print(f"Produto 2: R$ {preco_final_2:.2f}")
print(f"Produto 3: R$ {preco_final_3:.2f}")