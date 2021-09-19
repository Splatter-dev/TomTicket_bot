from google.cloud import dialogflow_v2
from google.api_core.exceptions import InvalidArgument
from whatsapp_tomticket.ext.config import  api_token


DIALOGFLOW_PROJECT_ID = api_token["DIALOG_FLOW_PROJ_ID"]
DIALOGFLOW_LANGUAGE_CODE = 'pt-BR'
GOOGLE_APPLICATION_CREDENTIALS = api_token["GOOGLE_APPLICATION_CREDENTIALS"]
SESSION_ID = '1234'



text_to_be_analyzed = "Olá"
session_client = dialogflow_v2.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
text_input = dialogflow_v2.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
query_input = dialogflow_v2.types.QueryInput(text=text_input)
try:
    response = session_client.detect_intent(session=session, query_input=query_input)
except InvalidArgument:
    raise
print("Query text:", response.query_result.query_text)
print("Detected intent:", response.query_result.intent.display_name)
print("Detected intent confidence:", response.query_result.intent_detection_confidence)
print("Detected response:", response.query_result.fulfillment_text)
    