# Exercício 7 — Aplicando OCP em cálculo de desconto

class Desconto:
    def calcular(self, valor):
        return 0

class DescontoComum(Desconto):
    def calcular(self, valor):
        return valor * 0.05

class DescontoVip(Desconto):
    def calcular(self, valor):
        return valor * 0.10

class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.15
    
# Adicionando um novo tipo de desconto sem modificar o código existente, apenas criando uma nova classe que herda de Desconto.
class DescontoPremiumPlus(Desconto):
    def calcular(self, valor):
        return valor * 0.20

def calcular_desconto(desconto: Desconto, valor: float):
    return desconto.calcular(valor)

# Exemplo de uso
valor_compra = 600.0
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto Comum: R$ {calcular_desconto(DescontoComum(), valor_compra):.2f}")
print(f"Desconto VIP: R$ {calcular_desconto(DescontoVip(), valor_compra):.2f}")
print(f"Desconto Premium: R$ {calcular_desconto(DescontoPremium(), valor_compra):.2f}")
print(f"Desconto Premium Plus: R$ {calcular_desconto(DescontoPremiumPlus(), valor_compra):.2f}")