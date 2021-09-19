from whatsapp_tomticket.ext.tom_ticket_api import TomTicket
from whatsapp_tomticket.ext.config import api_token


class Verification:
    def __init__(self):
        self.user_id_status = bool()
        self.first_menu_status = bool()
        self._user_data = ""
        self._first_menu = dict()
        self.evaluate = bool()
        self._user_opened_tickets = ""
        self.tom = TomTicket(api_token["TOMTICKET_TOKEN"])

    def greetings(self, msg: str) -> bool:
        """greetings [Verifica a primeira interação do cliente]

        Args:
            msg (str): [Primeira interação do cliente com o bot]

        Returns:
            bool: [Se a primeira interação do cliente é um cumprimento valido]
        """
        self.msg = msg
        self.greetings_words = [
            "oi",
            "olá",
            "ola",
            "bom dia",
            "boa tarde",
            "boa noite",
            "chamados",
        ]

        for word in self.greetings_words:
            if word in self.msg:
                self.evaluate = True
                break
            else:
                self.evaluate = False

        return self.evaluate

    def user_id(self, msg: str) -> bool:
        """user_id [Verifica se o usuario está cadastrado na base de dados]

        Args:
            msg (str): [Identificação enviada pelo o usuario: Email]

        Returns:
            bool: [Se o usuario existe ou na não na base de dados]
        """
        self._user_data = self.tom.get_cliente(str(msg))

        if not self._user_data["data"]:
            self.evaluate = False
        else:
            self.evaluate = True

        return self.evaluate

    def primary_menu_options(self, msg: str) -> bool:
        """primary_menu_options [Verifica qual a opção o usuario escolheu do menu]

        Args:
            msg (str): [Opção escolhida pelo o usuario]

        Returns:
            bool: [Se a opção escolhida pelo usuario é valida]
        """
        self._first_menu = {"1": "Listar chamados abertos", "2": "Criar um chamado"}

        if msg in self._first_menu:
            self.evaluate = True
        else:
            self.evaluate = False

        return self.evaluate

    def opened_tickets(self, tickets: dict) -> bool:
        """opened_tickets [Verifica se o cliente possui chamados abertos]

        Args:
            tickets (dict): [Dicionario contendo ou não os chamados abertos]

        Returns:
            bool: [Se o cliente possui chamados abertos]
        """
        self._user_opened_tickets = tickets

        if self._user_opened_tickets["total_itens"]:
            self.evaluate = True
        else:
            self.evaluate = False

        return self.evaluate
