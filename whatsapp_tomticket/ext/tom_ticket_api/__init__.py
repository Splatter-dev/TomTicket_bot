import requests
import json


class TomTicket:
    def __init__(self, token):
        self.idcliente = ""
        self.token = token
        self.url = "http://api.tomticket.com"
        self.headers = {"content-type": "application/x-www-form-urlencoded"}

    def listar_chamados(self, idcliente, page=1, tipo_identificacao="E"):
        self.idcliente = idcliente
        url = f"{self.url}/chamados/{self.token}/{page}?idcliente={self.idcliente}&tipo_identificacao={tipo_identificacao}&situacao=0,2,3"
        print(url)
        response = requests.get(url)
        return response.json()

    def ler_chamado(self, chamado):
        url = f"{self.url}/chamado/{self.token}/{chamado}"
        response = requests.get(url)
        return response.json()

    def get_clientes(self, page=1):
        url = f"{self.url}/clientes/{self.token}/{page}"
        response = requests.get(url)
        return response.json()

    def get_custom_fields(self):
        url = f"{self.url}/custom_fields/{self.token}"
        response = requests.get(url)
        return response.json()

    def get_organizations(self, page=1):
        url = f"{self.url}/organizacoes/{self.token}/{page}"
        response = requests.get(url)
        return response.json()

    def get_cliente(self, idcliente, tipo_identificador="E"):
        self.idcliente = idcliente
        url = f"{self.url}/cliente/detalhes/{self.token}/{self.idcliente}/{tipo_identificador}"
        response = requests.get(url)
        return response.json()

    def create_cliente(self, cliente):
        url = f"{self.url}/criar_cliente/{self.token}/"
        data = {
            "identificador": cliente.grid,
            "nome": cliente.name,
            "email": cliente.email,
            "criarchamados": cliente.can_create_order,
            "telefone": cliente.telephone,
            "id_organizacao": cliente.organization_id,
            "campos": cliente.fields,
        }
        response = requests.post(url, data=data, headers=self.headers)
        return response.json()

    def search_wiki(self, text):
        url = f"{self.url}/kb/busca/{self.token}/{text}"
        response = requests.get(url)
        return response.json()

    def create_client_quick_access(self, cliente, tipo="E"):
        url = f"{self.url}/criar_acesso_cliente/{self.token}"

        data = {"identificador": cliente, "tipo_identificacao": tipo}
        response = requests.post(url, data=data, headers=self.headers)
        return response.json()

    def update_cliente(self, identificador, cliente, tipo_identificador="E"):
        url = f"{self.url}/update_cliente/{self.token}/{identificador}/{tipo_identificador}"
        data = {
            "id_interno": cliente.grid,
            "nome": cliente.name,
            "email": cliente.email,
            "criarchamados": cliente.can_create_order,
            "telefone": cliente.telephone,
            "id_organizacao": cliente.organization_id,
            "campos": cliente.fields,
        }
        response = requests.post(url, data=data, headers=self.headers)
        return response.json()

    def inactive_cliente(self, identificador, tipo_identificador="E", active=False):
        url = f"{self.url}/customer/status/{self.token}/{identificador}/{tipo_identificador}"
        data = {"active": active}
        response = requests.post(url, data=data, headers=self.headers)
        return response.json()

    def start_chamado_status(self, ticket_id, status_id, comment):
        url = f"{self.url}/ticket/status/open/{self.token}"
        data = {"comment": comment, "ticket_id": ticket_id, "status_id": status_id}
        response = requests.post(url, data=data, headers=self.headers)
        return response.json()

    def close_chamado(self, ticket_id):
        url = f"{self.url}/ticket/status/close/{self.token}"
        data = {"ticket_id": ticket_id}
        response = requests.post(url, data=data, headers=self.headers)
        return response.json()

    def insert_comment(self, comment, ticket_id, attachment=None):
        url = f"{self.url}/ticket/comment/{self.token}"
        data = {"ticket_id": ticket_id, "comment": comment}
        if attachment is not None:
            data["attachment"] = attachment
        response = requests.post(url, data=data, headers=self.headers)
        return response.json()

    def get_departaments(self):
        url = f"{self.url}/departamentos/{self.token}"
        response = requests.get(url)
        return response.json()

    def criar_chamado(self, identificador, chamado):
        url = f"{self.url}/criar_chamado/{self.token}/{identificador}"
        response = requests.post(url, data=chamado, headers=self.headers)
        return response.json()

    def responder_chamado(self, chamado, mensagem, anexos=[]):
        url = f"{self.url}/chamado/{self.token}/{chamado}/responder"
        data = {"mensagem": mensagem, "anexos": anexos}
        response = requests.post(url, data=data, headers=self.headers)
        return response.json()

    def bloquear_clientes_abertura_chamados(self, cliente, bloquear=True):
        url = f"{self.url}/bloqueio_criacao_chamado/{self.token}/{cliente}"
        data = {"criarchamados": bloquear}
        response = requests.post(url, data=data, headers=self.headers)
        return response.json()

    def check_blacklist(self, endereco_email):
        url = f"{self.url}/blacklist/{self.token}/{endereco_email}"
        response = requests.get(url)
        return response.json()

    def criar_organizacao(
        self,
        nome,
        email="",
        telefone="",
        criar_chamados=False,
        chamadosgerente=False,
        chamadosmembros=False,
        limitechamadosmensal=0,
    ):
        url = f"{self.url}/criar_organizacao/{self.token}"
        data = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "criar_chamados": criar_chamados,
            "chamadosgerente": chamadosgerente,
            "chamadosmembros": chamadosmembros,
            "limitechamadosmensal": limitechamadosmensal,
        }
        response = requests.post(url, data=data, headers=self.headers)
        return response.json()

    def check_cliente(self, cliente):
        url = f"{self.url}/cliente/{self.token}/{cliente}"
        data = {"tipo_identificador": "E"}
        response = requests.get(url, data=data, headers=self.headers)
        return response.json()
