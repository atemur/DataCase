import requests
import json
from core.settings import BASE_URL, ENDPOINTS, start_date, end_date, organizationIDs
from api.auth import tgt

class Organisation:
    def __init__(self, org_id, tgt, endpoint):
        self.org_id = org_id
        self.tgt = tgt
        self.url = BASE_URL + endpoint
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "TGT": tgt
        }

    def registered_centrals(self, start_date, end_date):
        try:
            response = requests.post(
                url=self.url,
                headers=self.headers,
                data=json.dumps({
                    "startDate": str(start_date),
                    "endDate" : str(end_date),
                    "organizationId": self.org_id,
                })
            )
            return response.text
        except Exception as err:
            print(err)

"""    def get_uevcb(self):
    def live_santral(self):"""

for org_id in organizationIDs:
    organisation = Organisation(org_id=org_id, tgt=tgt, endpoint=ENDPOINTS["POWER_PLANTS"])
    data = organisation.registered_centrals(start_date, end_date)
    for x in json.loads(data)["items"]:
        print(f"Central Id: {x['id']}, EIC: {x['eic']}")
















