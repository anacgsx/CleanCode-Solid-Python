# Exercício 5 — Melhorando uma classe com muitos atributos soltos

class Cliente:
    def __init__(self, nome, email, telefone, cpf):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"CPF: {self.cpf}")

# Criando objetos da classe Cliente
cliente1 = Cliente("Ana Soares", "ana.soares@email.com", "(21) 99999-9999", "123.456.789-00")
cliente2 = Cliente("Carolina Gomes", "carolina.gomes@email.com", "(21) 88888-8888", "987.654.321-00")

# Exibindo dados dos clientes
print("\nCliente 1:")
cliente1.exibir_dados()
print("\nCliente 2:")
cliente2.exibir_dados()