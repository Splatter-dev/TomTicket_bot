from twilio.twiml.messaging_response import MessagingResponse

from os import environ
from flask import Flask, request, redirect, url_for

from whatsapp_tomticket.ext.config import flask_env
from whatsapp_tomticket.ext.verfications import Verification
from whatsapp_tomticket.ext.extract_data import ExtractDataFromApi
from whatsapp_tomticket.ext.trat_data import BeautifulStr
from whatsapp_tomticket.templates import Menus


app = Flask(__name__)
verify = Verification()
extract = ExtractDataFromApi()
parse_data = BeautifulStr()
menu = Menus()


@app.route("/bot", methods=["POST"])
def bot():

    incoming_msg = request.values.get("Body", "").lower()
    response = MessagingResponse()
    msg = response.message()

    if verify.greetings(incoming_msg):
        verify.user_id_status = False
        verify.first_menu_status = False
        msg.body(menu.welcome())

    elif not verify.user_id(incoming_msg) and not verify.user_id_status:
        msg.body(menu.invalid_user_id())

    elif verify.user_id(incoming_msg) and not verify.user_id_status:
        verify.user_id_status = True
        user_name = extract.user_name(incoming_msg)
        msg.body(menu.primary_options(user_name))

    elif verify.primary_menu_options(incoming_msg) and not verify.first_menu_status:
        verify.first_menu_status = True
        tickets_to_parse = extract.opened_tickets_or_creat(incoming_msg)
        tickets_status = verify.opened_tickets(tickets_to_parse)

        if tickets_status:
            parsed_opened_tickets = parse_data.parse_opened_tickets(tickets_to_parse)
            msg.body(menu.opened_user_tickets(parsed_opened_tickets ,tickets_status))
        else:
            msg.body(menu.user_without_opened_tickets)

    return str(response)


@app.route("/df", methods=["POST"])
def df():
    message = request.values.get("Body", "").lower()
    print(message)
    return message




if __name__ == "__main__":
    app.run()
