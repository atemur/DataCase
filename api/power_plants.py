import requests
import json
from core.settings import BASE_URL, ENDPOINTS, START_DATE, END_DATE
from api.auth import tgt

def get_santral_and_eic_by_orgId(organizationId, startDate, endDate, TGT):
    try:
        response = requests.post(
            url= BASE_URL + ENDPOINTS["POWER_PLANTS"],
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "TGT": TGT
            },
            data=json.dumps({
                "organizationId": organizationId,
                "startDate": str(startDate),
                "endDate" : str(endDate),
            })
        )
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    
start = START_DATE
end = END_DATE

"""list1 = get_santral_and_eic_by_orgId(13119, start, end, tgt)
list2 = get_santral_and_eic_by_orgId(7902, start, end, tgt)
list3 = get_santral_and_eic_by_orgId(4069, start, end, tgt)
list4 = get_santral_and_eic_by_orgId(20880, start, end, tgt)
list5 = get_santral_and_eic_by_orgId(16287, start, end, tgt)

for x in json.loads(list1)["items"]:
    print(x)
for x in json.loads(list2)["items"]:
    print(x)
for x in json.loads(list3)["items"]:
    print(x)
for x in json.loads(list4)["items"]:
    print(x)
for x in json.loads(list5)["items"]:
    print(x)"""