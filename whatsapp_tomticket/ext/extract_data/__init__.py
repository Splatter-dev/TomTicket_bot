from whatsapp_tomticket.ext.tom_ticket_api import TomTicket
from whatsapp_tomticket.ext.config import api_token


class ExtractDataFromApi:
    def __init__(self):
        self.tom = TomTicket(api_token["TOMTICKET_TOKEN"])
        self._user_data = ""
        self._user_name = ""
        self._user_id = ""
        self.tickets = dict()

    def user_name(self, user_id: str) -> str:
        """user_name [Extrai o nome do usuario]

        Args:
            user_id (str): [Id do usuario: Email]

        Returns:
            str: [O nome do usuario]
        """
        self._user_data = self.tom.get_cliente(user_id)
        self._user_id = self._user_data["data"]["email"]
        self._user_name = self._user_data["data"]["nome"]
        return self._user_name

    def opened_tickets_or_creat(self, chosed_option: str) -> dict:
        """opened_tickets_or_creat [Extrai chamados abertos do cliente]

        Args:
            chosed_option (str): [description]

        Returns:
            dict: [description]
        """
        options = {"Listar chamados abertos": "1", "Criar um chamado": "2"}

        if chosed_option in options["Listar chamados abertos"]:
            self.tickets = self.tom.listar_chamados(self._user_id)
            return self.tickets
