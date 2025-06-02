import requests
from core.settings import BASE_URL, ENDPOINTS
import json
from api.auth import tgt


def get_realtime_powerplants(TGT):    
    try:
        response = requests.get(
            url= BASE_URL + ENDPOINTS["REALTIME_PLANTS"],
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "TGT": TGT
            },
        )
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

data = get_realtime_powerplants(tgt)
for x in json.loads(data)["items"]:
    print(x)