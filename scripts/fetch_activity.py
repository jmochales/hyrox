import os, json, sys, ssl, time
from dotenv import load_dotenv

# Deshabilitar verificacion SSL (proxy corporativo con cert auto-firmado)
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['REQUESTS_CA_BUNDLE'] = ''
os.environ['SSL_CERT_FILE'] = ''
os.environ['PYTHONHTTPSVERIFY'] = '0'
ssl._create_default_https_context = ssl._create_unverified_context

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Parchear requests para no verificar SSL
import requests
old_request = requests.Session.request
def patched_request(self, *args, **kwargs):
    kwargs['verify'] = False
    return old_request(self, *args, **kwargs)
requests.Session.request = patched_request

# Parchear curl_cffi para no verificar SSL
try:
    import curl_cffi.requests as cffi_requests
    old_cffi_request = cffi_requests.Session.request
    def patched_cffi_request(self, *args, **kwargs):
        kwargs['verify'] = False
        return old_cffi_request(self, *args, **kwargs)
    cffi_requests.Session.request = patched_cffi_request
except ImportError:
    pass

from garminconnect import Garmin

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
email = os.getenv('GARMIN_EMAIL')
password = os.getenv('GARMIN_PASSWORD')

activity_id = int(sys.argv[1]) if len(sys.argv) > 1 else 23666559351

print(f"Conectando a Garmin Connect...")
client = Garmin(email, password)
client.login()
print(f"Login OK. Consultando actividad {activity_id}...")

activity = client.get_activity(activity_id)
print("=== ACTIVIDAD ===")
print(json.dumps(activity, indent=2, default=str))

# Intentar obtener exercise sets
try:
    exercise_sets = client.get_activity_exercise_sets(activity_id)
    print("\n=== EXERCISE SETS ===")
    print(json.dumps(exercise_sets, indent=2, default=str))
except Exception as e:
    print(f"\nNo se pudieron obtener exercise sets: {e}")

# Intentar obtener splits/laps
try:
    splits = client.get_activity_splits(activity_id)
    print("\n=== SPLITS ===")
    print(json.dumps(splits, indent=2, default=str))
except Exception as e:
    print(f"\nNo se pudieron obtener splits: {e}")
