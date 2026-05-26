# Exercício 15 — Mini projeto: sistema de pedidos aplicando Clean Code e SOLID

from abc import ABC, abstractmethod

# Entidades do sistema:
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco   

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_subtotal(self):
        return self.produto.preco * self.quantidade
    
# Serviço de desconto:
class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class DescontoComum(Desconto):
    def calcular(self, valor):
        return valor * 0.05
    
# Pagamento:
class FormaPagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class CartaoCredito(FormaPagamento):
    def pagar(self, valor):
        return f"Pagando R$ {valor:.2f} com cartão de crédito."
    
class Pix(FormaPagamento):
    def pagar(self, valor):
        return f"Pagando R$ {valor:.2f} via Pix."
    
# Notificação:
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

class EmailService(Notificador):
    def enviar(self, mensagem):
        return f"Enviando e-mail: {mensagem}"
    
# Pedido:
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.desconto = DescontoComum()
        self.forma_pagamento = None
        self.notificador = EmailService()

    def adicionar_item(self, produto, quantidade):
        self.itens.append(ItemPedido(produto, quantidade))

    def calcular_subtotal(self):
        subtotal = 0
        for item in self.itens:
            subtotal += item.calcular_subtotal()
        return subtotal

    def aplicar_desconto(self):
        subtotal = self.calcular_subtotal()
        return subtotal - self.desconto.calcular(subtotal)

    def processar_pagamento(self, forma_pagamento):
        self.forma_pagamento = forma_pagamento
        valor_final = self.aplicar_desconto()
        return self.forma_pagamento.pagar(valor_final)

    def enviar_notificacao(self, mensagem):
        return self.notificador.enviar(mensagem)
    
# Exemplo de uso do sistema:
cliente = Cliente("Ana Carolina", "anacgs@email.com")
produto1 = Produto("Macbook", 12000.00)
produto2 = Produto("Monitor 4k", 800.00)

pedido = Pedido(cliente)
pedido.adicionar_item(produto1, 1)
pedido.adicionar_item(produto2, 1)

print(f"Subtotal: R$ {pedido.calcular_subtotal():.2f}")
print(f"Desconto: R$ {pedido.desconto.calcular(pedido.calcular_subtotal()):.2f}")
print(f"Total: R$ {pedido.aplicar_desconto():.2f}")
print(pedido.processar_pagamento(Pix()))
print(pedido.enviar_notificacao("Seu pedido foi processado com sucesso!"))