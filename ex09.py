# Exercício 9 — Evitando violação do LSP

class Ave:
    def andar(self):
        print("Ave andando")

    def bicar(self):
        print("Ave bicando")


class AvesQueVoam(Ave):
    def voar(self):
        print("Voando")


class BemTeVi(AvesQueVoam):
    pass


class Pinguim(Ave):
    pass


bemTeVi = BemTeVi()
bemTeVi.voar()

pinguim = Pinguim()
pinguim.andar()
pinguim.bicar()