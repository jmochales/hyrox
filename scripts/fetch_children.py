import time
import os, json, sys, ssl

# Deshabilitar verificacion SSL
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['REQUESTS_CA_BUNDLE'] = ''
os.environ['SSL_CERT_FILE'] = ''
os.environ['PYTHONHTTPSVERIFY'] = '0'
ssl._create_default_https_context = ssl._create_unverified_context

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
old_request = requests.Session.request
def patched_request(self, *args, **kwargs):
    kwargs['verify'] = False
    return old_request(self, *args, **kwargs)
requests.Session.request = patched_request

try:
    import curl_cffi.requests as cffi_requests
    old_cffi_request = cffi_requests.Session.request
    def patched_cffi_request(self, *args, **kwargs):
        kwargs['verify'] = False
        return old_cffi_request(self, *args, **kwargs)
    cffi_requests.Session.request = patched_cffi_request
except ImportError:
    pass

from dotenv import load_dotenv
from garminconnect import Garmin

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
email = os.getenv('GARMIN_EMAIL')
password = os.getenv('GARMIN_PASSWORD')

print("Esperando 120s por rate limit...")
time.sleep(120)

print("Conectando a Garmin Connect...")
client = Garmin(email, password)
client.login()
print("Login OK.")

child_ids = [23670660357, 23670660354, 23670700075, 23670700077, 23670700076, 23670700078]

for cid in child_ids:
    print(f"\n=== ACTIVIDAD {cid} ===")
    try:
        activity = client.get_activity(cid)
        summary = activity.get('summaryDTO', {})
        print(json.dumps({
            'activityId': cid,
            'activityName': activity.get('activityName'),
            'activityType': activity.get('activityTypeDTO', {}).get('typeKey'),
            'startTimeLocal': summary.get('startTimeLocal'),
            'duration': summary.get('duration'),
            'distance': summary.get('distance'),
            'averageHR': summary.get('averageHR'),
            'calories': summary.get('calories'),
            'averageSpeed': summary.get('averageSpeed'),
            'description': activity.get('description'),
        }, indent=2, default=str))
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(2)
