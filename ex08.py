# Exercício 8 — Aplicando LSP em formas geométricas

class FormaGeometrica:
    def calcularArea(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularArea(self):
        return self.largura * self.altura

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado ** 2

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return 3.14159 * self.raio ** 2

def calcularAreas(formas: list[FormaGeometrica]):
    for forma in formas:
        print(f"A área do {forma.__class__.__name__} é: {forma.calcularArea()}")

# Exemplo de uso
formas = [
    Retangulo(4, 5),
    Quadrado(4.5),
    Circulo(2.55)
]
calcularAreas(formas)