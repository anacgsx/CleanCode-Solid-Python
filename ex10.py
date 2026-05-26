# Exercício 10 — Aplicando ISP em dispositivos eletrônicos

from abc import ABC, abstractmethod

class DispositivoEletronico(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class DispositivoQueImprime(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class DispositivoQueEscaneia(ABC):
    @abstractmethod
    def escanear(self):
        pass

class ImpressoraMultifuncional(
    DispositivoEletronico, 
    DispositivoQueImprime, 
    DispositivoQueEscaneia
    ):
    def ligar(self):
        print("Impressora ligada.")

    def desligar(self):
        print("Impressora desligada.")

    def imprimir(self):
        print("Imprimindo documento...")

    def escanear(self):
        print("Escaneando documento...")

class Lampada(DispositivoEletronico):
    def ligar(self):
        print("Lâmpada ligada.")

    def desligar(self):
        print("Lâmpada desligada.")

lampada = Lampada()
lampada.ligar()

impressora = ImpressoraMultifuncional()
impressora.ligar()
impressora.imprimir()
impressora.escanear()