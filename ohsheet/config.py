import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

config = json.loads(open("config.json", "r").read())

scope = config['scope']
creds = ServiceAccountCredentials.from_json_keyfile_dict(config['client-secret'], scope)
gsclient = gspread.authorize(creds)