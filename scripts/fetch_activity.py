import os, json, sys, ssl, urllib3
from dotenv import load_dotenv
from garminconnect import Garmin

# Deshabilitar verificacion SSL (proxy corporativo con cert auto-firmado)
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['REQUESTS_CA_BUNDLE'] = ''
os.environ['SSL_CERT_FILE'] = ''
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
email = os.getenv('GARMIN_EMAIL')
password = os.getenv('GARMIN_PASSWORD')

activity_id = int(sys.argv[1]) if len(sys.argv) > 1 else 23666559351

client = Garmin(email, password)
client.login()

activity = client.get_activity(activity_id)
print(json.dumps(activity, indent=2, default=str))
