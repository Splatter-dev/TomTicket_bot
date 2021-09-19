import os
from dotenv import load_dotenv

load_dotenv()

api_token = {
    "TWILIO_TOKEN": os.getenv("TWILIO_TOKEN"),
    "TOMTICKET_TOKEN": os.getenv("TOMTICKET_TOKEN"),
    "GOOGLE_APPLICATION_CREDENTIALS": os.getenv("GOOGLE_APPLICATION_CREDENTIALS"),
    "DIALOG_FLOW_PROJ_ID": os.getenv("DIALOG_FLOW_PROJ_ID")
}

flask_env = {"ENV": os.getenv("FLASK_ENV"), "APP": os.getenv("FLASK_APP")}
