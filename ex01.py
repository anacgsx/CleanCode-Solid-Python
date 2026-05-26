#Exercício 1 — Nomes significativos

def calcular_valor_total(quantidade_itens, preco_unitario):
    return quantidade_itens * preco_unitario

#Exemplo de uso da função:

quantidade = int(input("Digite a quantidade de itens: "))
preco = float(input("Digite o preço unitário: "))
valor_total = calcular_valor_total(quantidade, preco)
print(f"Valor total da compra: R$ {valor_total:.2f}")