# Libs
import json
import os
from google.oauth2 import service_account

# Gets the google credentials from .env and formats them for the google libs
def google_credentials():
  google_service_account_json_secret = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
  if google_service_account_json_secret is None:
    raise Exception("GOOGLE_SERVICE_ACCOUNT_JSON secret does not exist")
  else:
    google_service_account_json = json.loads(google_service_account_json_secret)
    return service_account.Credentials.from_service_account_info(
      google_service_account_json
    )

# In google's infinite wisdom (and laziness) I can't actually use a service account
# for google maps api, so I have to have *another* key
def google_maps_key():
  google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")
  if google_maps_api_key is None:
    raise Exception("GOOGLE_MAPS_API_KEY secret does not exist")
  else:
    return google_maps_api_key