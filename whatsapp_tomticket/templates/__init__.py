from operator import itemgetter

from whatsapp_tomticket.ext.trat_data import BeautifulStr


class Menus:
    def __init__(self):
        self.parse_data = BeautifulStr()
        self.msg = ""
        self.tickets_status = ""
        self.opened_tickets = ""
        self.formated_opened_tickets = ""

    def welcome(self):
        self.msg = f"Por favor, digite seu endereço de e-mail."
        return self.msg

    def invalid_user_id(self):
        self.msg = f"E-mail invalido. Digite novamente."
        return self.msg

    def primary_options(self, user_name):
        self.user_name = user_name

        self.msg = f"Olá, *{self.user_name}* 🤓.\
            \n\nEssas são as opções:\n\n\
            *1 - Listar chamados abertos*\n\
            *2 - Criar um chamado*"
        return self.msg

    def _format_opened_tickets(self, tickets):
        opened_tickets = tickets
        opened_tickets_menu = "⚠️  *CHAMADOS ABERTOS*  ⚠️\n\n"

        for ticket_info in opened_tickets:

            opened_tickets_menu += f"🎫 *{ticket_info[0]}* *-* *{ticket_info[1]}* 🎫\
                \n\n*Mensagem:* {self.parse_data.parse_first_message(ticket_info[2])}\
                \n*Categoria:* {ticket_info[3]}\
                \n*Protocolo:* {ticket_info[4]}\
                \n*Data de abertura:* {ticket_info[5]}\
                \n*Data da ultima intereção:* {ticket_info[6]}\
                \n*Status:* {ticket_info[7]}\
                \n\n"
        return opened_tickets_menu

    def opened_user_tickets(self, tickets, tickets_status):
        self.tickets_status = tickets_status

        if self.tickets_status:
            self.opened_tickets = tickets
            self.formated_opened_tickets = self._format_opened_tickets(
                self.opened_tickets
            )
            return self.formated_opened_tickets
        else:
            return "Não tem chamados abertos"

    def user_without_opened_tickets(self):
        return "Você não tem chamados abertos."
        
        