import requests
from config.settings import BASE_URL, ENDPOINTS

class OrganisationClient:
    def __init__(self, tgt_token, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "TGT": tgt_token
        }

    def fetch_registered_powerplants(self, org_id):
        try:
            url = BASE_URL + ENDPOINTS["POWER_PLANTS"]
            data = {
                "startDate": self.start_date,
                "endDate": self.end_date,
                "organizationId": org_id,
            }
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json().get('items', [])
        except Exception as err:
            print(err)
            return []

    def fetch_uevcbs_by_powerplant_id(self, powerplant_id):
        try:
            url = BASE_URL + ENDPOINTS["UEVCB_LIST"]
            data = {
                "startDate": self.start_date,
                "endDate": self.end_date,
                "powerPlantId": powerplant_id
            }
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json().get("items", [])
        except Exception as err:
            print(err)
            return []

    def fetch_realtime_powerplants(self):
        try:
            url = BASE_URL + ENDPOINTS["REALTIME_PLANTS"]
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json().get("items", [])
        except Exception as err:
            print(err)
            return []
