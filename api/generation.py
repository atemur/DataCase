import requests
from config.settings import BASE_URL, ENDPOINTS

class GenerationClient:
    def __init__(self, tgt_token, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "TGT": tgt_token
        }

    def fetch_realtime_generation(self, gzu_id):
        try:
            url = BASE_URL + ENDPOINTS["REALTIME_GEN"]
            data = {
                "startDate": self.start_date,
                "endDate": self.end_date,
                "powerPlantId": gzu_id
            }
            response = requests.post(url, headers=self.headers, json=data)
            return response.json().get("items", [])
        except Exception as err:
            print(err)
            return []

    def fetch_dpp(self, region, uevcb_id):
        try:
            url = BASE_URL + ENDPOINTS["DPP"]
            data = {
                "startDate": self.start_date,
                "endDate": self.end_date,
                "region": region,
                "uevcbId": uevcb_id
            }

            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json().get("items", [])
        except Exception as err:
            print(err)
            return []
