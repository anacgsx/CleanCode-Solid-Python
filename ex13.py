# Exercício 13 — Sistema de biblioteca com Clean Code

from datetime import datetime

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Emprestimo:
    def __init__(self, aluno, livro, data_emprestimo):
        self.aluno = aluno
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.devolver = False

    def marcar_como_devolvido(self):
        self.devolver = True

class Biblioteca:
    def __init__(self):
        self.emprestimos = []

    def registrar_emprestimo(self, aluno, livro):
        emprestimo = Emprestimo(aluno, livro, datetime.now())
        self.emprestimos.append(emprestimo)

    def listar_emprestimos_ativos(self):
        for emprestimo in self.emprestimos:
            if not emprestimo.devolver:
                print(f"Aluno: {emprestimo.aluno.nome}, Livro: {emprestimo.livro.titulo}, Data: {emprestimo.data_emprestimo}")

# Exemplo de uso do sistema:
biblioteca = Biblioteca()   

aluno1 = Aluno("Carolina Soares", "2023221")
livro1 = Livro("Clean Code", "Robert C. Martin")
aluno2 = Aluno("Ana Gomes", "2023222")
livro2 = Livro("Entendendo Algoritmos", "Aditya Y. Bhargava")

biblioteca.registrar_emprestimo(aluno1, livro1)
biblioteca.registrar_emprestimo(aluno2, livro2)

print("Empréstimos ativos:")
biblioteca.listar_emprestimos_ativos()

devolver = biblioteca.emprestimos[0] # Supondo que o primeiro empréstimo seja devolvido

devolver.marcar_como_devolvido()

print("\nApós marcar como devolvido:")
biblioteca.listar_emprestimos_ativos()