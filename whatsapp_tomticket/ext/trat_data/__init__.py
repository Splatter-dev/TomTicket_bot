from bs4 import BeautifulSoup
from operator import itemgetter


class BeautifulStr:
    def __init__(self):
        self.parsed_opened_tickets = []
        self.parsed_first_message = ""

    def parse_opened_tickets(self, tickets_to_parse: dict) -> list:
        """parse_opened_tickets [Faz o tratamento dos chamados vindo do Tomticket]

        Args:
            tickets_to_parse (dict): [Dict contendo informações sobre os chamados]

        Returns:
            list: [Com os dados filtrados e indice]
        """
        tickets_info_to_filter = tickets_to_parse["data"]
        tickets_list_filtered = []
        for index, ticket in enumerate(tickets_info_to_filter):
            tickets_list = list(
                itemgetter(
                    "titulo",
                    "mensagem",
                    "categoria",
                    "protocolo",
                    "data_criacao",
                    "dataultimasituacao",
                    "descsituacao",
                    "idchamado",
                )(ticket)
            )
            tickets_list.insert(0, index + 1)
            tickets_list_filtered.append(tickets_list)
            
        self.parsed_opened_tickets = tickets_list_filtered
        print(tickets_list_filtered)
        return self.parsed_opened_tickets

    def parse_first_message(self, message: str) -> str:
        """parse_first_message [Faz o parse da primeira menssagem do chamado usando
        a lib BeautifulSoup, remove os caracteres como "\n" usando split e join
        e remove um parte da mensagem se ela tiver mais de 33 caracteres]

        Args:
            message (str): [primeira mensagem do chamado]

        Returns:
            str: [mensagem tratada]
        """
        first_message_limit = 33
        parsed_message = BeautifulSoup(message, "lxml").get_text(strip=True)
        self.parsed_first_message = " ".join(parsed_message.split())

        if len(self.parsed_first_message) > first_message_limit:
            self.parsed_first_message = self.parsed_first_message[0:33]
            self.parsed_first_message += "..."

        return self.parsed_first_message
