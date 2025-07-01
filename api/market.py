import requests
from config.settings import BASE_URL, ENDPOINTS

class MarketClient:
    def __init__(self, tgt_token, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "TGT": tgt_token
        }

    def fetch_dam_quantities(self, organization_id):
        try:
            url = BASE_URL + ENDPOINTS["DAM_CLEARING"]
            data = {
                "startDate": self.start_date,
                "endDate": self.end_date,
                "organizationId": organization_id
            }
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json().get("items", [])
        except Exception as err:
            print(err)
            return []

    def fetch_idm_quantities(self, organization_id):
        try:
            url = BASE_URL + ENDPOINTS["IDM_MATCHING"]
            data = {
                "startDate": self.start_date,
                "endDate": self.end_date,
                "organizationId": organization_id
            }
            response = requests.post(url=url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json().get("items", [])
        except Exception as err:
            print(err)
            return []

    def fetch_bilateral_bids(self, organization_id):
        try:
            url = BASE_URL + ENDPOINTS["BILATERAL_BID"]
            data = {
                "startDate": self.start_date,
                "endDate": self.end_date,
                "organizationId": organization_id
            }
            response = requests.post(url=url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json().get("items", [])
        except Exception as err:
            print(err)
            return []

    def fetch_bilateral_offers(self, organization_id):
        try:
            url = BASE_URL + ENDPOINTS["BILATERAL_OFFER"]
            data = {
                "startDate": self.start_date,
                "endDate": self.end_date,
                "organizationId": organization_id
            }
            response = requests.post(url=url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json().get("items", [])
        except Exception as err:
            print(err)
            return []
