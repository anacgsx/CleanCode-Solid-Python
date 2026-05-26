# Exercício 11 — Aplicando DIP em envio de notificações

from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

class EmailService(Notificador):
    def enviar(self, mensagem):
        print("Enviando e-mail:", mensagem)

class SMSService(Notificador):
    def enviar(self, mensagem):
        print("Enviando SMS:", mensagem)

class Pedido:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador

    def finalizar(self):
        self.notificador.enviar("Pedido finalizado com sucesso.")


pedido_email = Pedido(EmailService())
pedido_email.finalizar()

pedido_sms = Pedido(SMSService())
pedido_sms.finalizar()