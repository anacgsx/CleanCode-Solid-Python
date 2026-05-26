# Exercício 6 — Aplicando SRP em um sistema de relatório

class GerarDados:
    def gerar(self):
        return ["Produto A", "Produto B", "Produto C"]

class FormatarRelatorio:
    def formatar(self, dados):
        return "\n".join(dados)

class SalvarArquivo:
    def salvar(self, conteudo):
        with open("relatorio.txt", "w") as arquivo:
            arquivo.write(conteudo)

# Exemplo de uso:
if __name__ == "__main__":
    gerador = GerarDados()
    formatador = FormatarRelatorio()
    salvador = SalvarArquivo()

    dados = gerador.gerar()
    relatorio_formatado = formatador.formatar(dados)
    salvador.salvar(relatorio_formatado)

    print("Relatório gerado e salvo com sucesso.")