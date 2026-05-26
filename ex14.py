# Exercício 14 — Refatorando sistema de pagamento

from abc import ABC, abstractmethod

class FormaPagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class PagamentoCartao(FormaPagamento):
    def pagar(self, valor):
        print(f"Pagamento de R$ {valor} realizado no cartão.")

class PagamentoPix(FormaPagamento):
    def pagar(self, valor):
        print(f"Pagamento de R$ {valor} realizado via Pix.")

class PagamentoBoleto(FormaPagamento):
    def pagar(self, valor):
        print(f"Boleto gerado no valor de R$ {valor}.")

class ProcessarPagamento:
    def __init__(self, forma_pagamento: FormaPagamento):
        self.forma_pagamento = forma_pagamento

    def processar(self, valor):
        self.forma_pagamento.pagar(valor)

# Exemplo de uso:
valor_pagamento = 150.00
forma_pagamento = PagamentoCartao()

processar_pagamento = ProcessarPagamento(forma_pagamento)
processar_pagamento.processar(valor_pagamento)