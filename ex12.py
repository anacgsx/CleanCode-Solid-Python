# Exercício 12 — Refatorando um cadastro de produtos

class Produto:
    def __init__(self, nome: str, preco: float, categoria: str, estoque: int):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.estoque = estoque


class GerenciarProdutos:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"Nome: {produto.nome}, Preço: R$ {produto.preco:.2f}, Categoria: {produto.categoria}, Estoque: {produto.estoque}")

    def calcular_valor_total_estoque(self) -> float:
        total = 0
        for produto in self.produtos:
            total += (produto.preco * produto.estoque)
        return total
    
# Exemplo de uso do sistema:
produto1 = Produto("Notebook", 4500.00, "Eletrônicos", 10)
produto2 = Produto("Smartphone", 3500.00, "Eletrônicos", 20)

gerenciador = GerenciarProdutos() 

gerenciador.cadastrar_produto(produto1)
gerenciador.cadastrar_produto(produto2)

print("Produtos cadastrados:")
gerenciador.listar_produtos()
print(f"Valor total em estoque: R$ {gerenciador.calcular_valor_total_estoque():.2f}")